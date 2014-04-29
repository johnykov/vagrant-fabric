from fabric.api import task, run
from fabric.contrib.files import uncomment

from fabtools import require, deb
from fabtools.vagrant import vagrant

@task
def provision():
    require.deb.key('7F0CEB10', keyserver='keyserver.ubuntu.com')
    require.deb.source('mongodb', 'http://downloads-distro.mongodb.org/repo/ubuntu-upstart', 'dist', '10gen')
    require.deb.packages([
        'mongodb-10gen',
        ], update=True)