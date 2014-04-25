from fabric.api import task, settings
from fabric.contrib.files import comment
from fabtools.vagrant import vagrant
from fabtools import require, deb, oracle_jdk, python, tomcat
from fabtools.utils import run_as_root
from fabtools.mysql import _query

@task
def updateIndex():
    deb.update_index()
    
@task
def provision():
    updateIndex()
    require.file('.vimrc', source='vimrc')
    # install java7
    require.oracle_jdk.installed()
    # install tomcat7
    require.tomcat.installed()
    # install other packages
    require.deb.packages([
        'build-essential',
        'python'
        ], update=True)
    deb.upgrade()

@task
def installMySql():
    updateIndex()
    # install mysql
    require.mysql.server(password='s3cr3t')
    with settings(mysql_user='root', mysql_password='s3cr3t'):
        require.mysql.user('dbuser', 'bar')
        require.mysql.database('foo', owner='dbuser')
    configMySqlToAllowOutsideConnection()

@task
def configMySqlToAllowOutsideConnection():
    comment('/etc/mysql/my.cnf', r'^bind-address', use_sudo=True)
    _query("GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 's3cr3t';",mysql_user='root', mysql_password='s3cr3t')
    run_as_root("service mysql restart")

@task
def installMongo():
    require.deb.key('7F0CEB10', keyserver='keyserver.ubuntu.com')
    require.deb.source('mongodb', 'http://downloads-distro.mongodb.org/repo/ubuntu-upstart', 'dist', '10gen')
    # deb.update_index()
    require.deb.packages([
        'mongodb-10gen',
        ], update=True)

@task
def installTomcat():
    require.oracle_jdk.installed()
    # install tomcat
    # require.tomcat.installed('6.0.36')
    require.tomcat.installed()

@task
def startTomcat():
    tomcat.start_tomcat()

