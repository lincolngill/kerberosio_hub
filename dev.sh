#!/usr/bin/env bash

CMD=$(echo ${1:-run} | tr '[A-Z]' '[a-z]')
IMGNAME="kerberosio_hub"
VER="0.1"
NAMESPACE="links10"
TAG="${NAMESPACE}/${IMGNAME}:${VER}"
CONTNAME="${IMGNAME}"
RESTART="--restart unless-stopped"

cd $(dirname $0)
case $CMD in
    build)
        set -x
        docker build --tag ${TAG} .
        docker image list
        set +x
        ;;
    run)
        set -x
        docker run ${RESTART} --detach --publish 8080:8080 --name ${CONTNAME} ${TAG}
        docker container list --all
        set +x
        ;;
    stop)
        set -x
        docker stop ${CONTNAME}
        docker rm ${CONTNAME}
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
        docker push ${TAG}
        set +x
        ;;
    ps)
        set -x
        docker ps
        set +x
        ;;
    *)
        echo "Invalid command arg: $CMD" >&2
        exit 1
        ;;
esac