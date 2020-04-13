#!/usr/bin/env bash
#
# Setup build env
#
# source this file

function ds_set () {
    # Environment variables with default values based on project directory
    DS_PROJDIR="${DS_PROJDIR:-$(cd $(dirname $BASH_SOURCE); pwd)}"
    DS_PROJ="${DS_PROJ:-$(basename ${DS_PROJDIR})}"
    DS_IMGNAME="${DS_IMGNAME:-$DS_PROJ}"
    DS_VER="${DS_VER:-0.2}"
    DS_NAMESPACE="${DS_NAMESPACE:-links10}"
    DS_TAG="${DS_TAG:-${DS_NAMESPACE}/${DS_IMGNAME}}"
    DS_CONTNAME="${DS_CONTNAME:-${DS_IMGNAME}}"
    DS_RESTART="${DS_RESTART:---restart unless-stopped}"
}

echo "Docker Shortcut (ds) command setup"

# Show env settings
function ds_show () {
    for V in DS_PROJ DS_PROJDIR DS_IMGNAME DS_VER DS_NAMESPACE DS_TAG DS_CONTNAME DS_RESTART
    do
 	printf "%14s: %s\n" $V "${!V}"
    done
}

# unset env settings
function ds_unset () {
    for V in DS_PROJ DS_PROJDIR DS_IMGNAME DS_VER DS_NAMESPACE DS_TAG DS_CONTNAME DS_RESTART
    do
	unset $V
    done
}

# Activate python virtual env 
# Don't actually need this if developing using Flask debug in docker
# Need to install modules into env with: pip install -r requirements.txt
function ds_activate () {
    PROJ="${1:-${DS_PROJ}}"
    if [ -x /usr/local/bin/virtualenvwrapper.sh ]; then
        echo "Python virtual env: $PROJ"
        . /usr/local/bin/virtualenvwrapper.sh
        workon $PROJ
    fi
}

# Docker shortcut function ds
function ds () {
    CMD="$(echo ${1:-run} | tr '[A-Z]' '[a-z]')"

    case $CMD in
        activate)
            ds_set
            ds_show
            ds_activate "$DS_PROG"
            cd ${DS_PROJDIR}
            ;;
        build)
            set -x
            docker build --tag ${DS_TAG} .
            docker image list
            set +x
            ;;
        devrun)
            set -x
                docker run --detach --publish 8080:8080 --volume ${DS_PROJDIR}/src:/src -e FLASK_DEBUG=Y --name ${DS_CONTNAME} ${DS_TAG}
                docker container list --all
            set +x
            ;;
        run)
            set -x
            docker run ${DS_RESTART} --detach --publish 8080:8080 --name ${DS_CONTNAME} ${DS_TAG}:${DS_VER}
            docker container list --all
            set +x
            ;;
        stop)
            set -x
            docker stop ${DS_CONTNAME}
            docker rm ${DS_CONTNAME}
            docker container list --all
            set +x
            ;;
        clean)
            set -x
            # Remove all exited containers
            docker container rm $(docker container list --filter status=exited --quiet)
            docker container list --all
            set +x
            ;;
        push)
            set -x
            docker login
            docker push ${DS_TAG}:${DS_VER}
            set +x
            ;;
        ps)
            set -x
            docker ps
            set +x
            ;;
	    deactivate)
            ds_unset
            ds_show
            deactivate
            ;;
        show) ds_show ;;
        *)
            echo "Invalid command arg: $CMD" >&2
            exit 1
            ;;
    esac
}

ds activate