# kerberosio_hub
Central command hub for Kerberos.io security camera agents

## Howto Run Container in Develop Mode

The ```setup_env.sh``` script sets up bash shortcut functions for development and build activities:
* Activates a pre-created python virtual env if ```virtualenvwrapper``` is installed
* Refer to the script for functionality

E.g.

```bash
links@skynet10:~/Documents/pizero_camera/kerberosio_hub$ . ./setup_env.sh
```
Once run the docker shortcut command, ```ds``` is available.

Run the container in dev mode to make development easier:
* Maps project ```src``` directory as a volume
* Runs Flask app with ```debug=true```
* Can edit source and should see immediate changes
* Need to rebuild image to update ```/src``` within container

```bash
(kerberosio_hub) links@skynet10:~/Documents/pizero_camera/kerberosio_hub$ ds devrun
```

Important: The ```ds``` docker shortcut command uses DS_* environment variables. ```setup_env.sh``` will not change these, if already set.

To revert to the calculated default DS_* values:

```bash
(kerberosio_hub) links@skynet10:~/Documents/pizero_camera/kerberosio_hub$ ds deactivate
links@skynet10:~/Documents/pizero_camera/kerberosio_hub$ ds activate
```

This enables you to set the DS_* variables to override the calculated defaults. Either before or after ```setup_env.sh``` is run. 