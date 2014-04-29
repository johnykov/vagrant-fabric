from fabric.api import task, sudo
from fabric.contrib.files import comment

from fabtools import require, tomcat
from fabtools.vagrant import vagrant

@task
def provision():
    # require java
    require.oracle_jdk.installed(version='7u55-b13')
    # require tomcat
    require.tomcat.installed('7.0.53')

@task
def deploySample():
    tomcat.deploy_application('sample.war')