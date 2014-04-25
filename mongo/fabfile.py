from fabric.api import *
from fabtools.vagrant import vagrant
from fabtools import require, deb

@task
def provision():
    installMongo()

@task
def installMongo():
    require.deb.key('7F0CEB10', keyserver='keyserver.ubuntu.com')
    require.deb.source('mongodb', 'http://downloads-distro.mongodb.org/repo/ubuntu-upstart', 'dist', '10gen')
    require.deb.packages([
        'mongodb-10gen',
        ], update=True)