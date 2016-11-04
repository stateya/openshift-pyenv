=======================================================================
  Openshift pyenv
=======================================================================


Install
====================================
Intall with default python version(3.5.2)

::

  (Your PC)$ rhc create-app app diy-0.1
  (Your PC)$ cd app
  (Your PC)$ git remote add upstream https://github.com/stateya/openshift-pyenv
  (Your PC)$ git pull -s recursive -X ours upstream master
  (Your PC)$ git push origin master


Change Python vesion
====================================

::

  (Your PC)$ echo '2.7.9' > <repo dir>/.python-version # change 2.7.9
  (Your PC)$ git add .
  (Your PC)$ git commit -m 'change python version'
  (Your PC)$ git push origin master # long time...

Error for long time
======================================

::

  remote: Downloading Python-3.5.2.tar.xz...
  remote: -> https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tar.xz
  remote: Installing Python-3.5.2...
  remote: patching file Lib/venv/scripts/posix/activate.fish
  Connection to <app-name>-<name>.rhcloud.com closed by remote host.
  fatal: The remote end hung up unexpectedly
  error: error in sideband demultiplexer
  To ssh://<user>@<app-name>-<name>.rhcloud.com/~/git/<app-name>.git/
     xxxx..xxxxx  master -> master
  error: failed to push some refs to 'ssh://<user>@<app-name>-<name>.rhcloud.com/~/git/<app-name>.git/'


Do this when the above

- change something,git push
- execute rebuild_pyenv_install command on OpenShift Server

rebuild_pyenv_install command

::

  (OpenShift Server$ app-root/repo/.openshift/diy/rebuild_pyenv_install


Library
====================================

::

  (Your PC)$ pip install pyenv
  (Your PC)$ pip freeze > <repo dir>/requirements.txt

Develop Application
=====================================

Change <repo dir>/diy/.


SSH for debug
======================================

::

  (OpenShift Server)$ source app-root/data/venv/bin/activate
