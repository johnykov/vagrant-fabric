from fabric.api import task,sudo,settings
from fabric.contrib.files import comment

from fabtools import require, files, mysql
from fabtools.vagrant import vagrant

@task
def provision():        
    # install required packages (+extras) for LAMP server
    require.deb.packages([
        # 'build-essential',
        # 'devscripts',
        'locales',
        'apache2',
        'php5',
        'php5-mysql',        
    ], update=True)
       
    # change Apache envvars and set vagrant has main user
    require.files.template_file(
        template_source = './fabric/files/apache/envvars.template',
        path='/etc/apache2/envvars', 
        context = {
            'apache_run_user': 'vagrant',
            'apache_run_group': 'vagrant',
        },
        owner = 'root',
        group = 'root',
        use_sudo=True
    )

    # create a new virtual host and use ~/vagrant_www as document root
    require.files.template_file(
        template_source = './fabric/files/apache/vhost.conf.template',
        path='/etc/apache2/sites-available/vagrant', 
        context = {
            'server_name': 'localhost',
            'port': 80,
            'document_root': '/vagrant',
        },
        owner = 'root',
        group = 'root',
        use_sudo=True
    )

    # enable new vhost
    if not files.is_link('/etc/apache2/sites-enabled/vagrant'):
        sudo("a2dissite default")
        sudo("a2ensite vagrant")

    # activate mod_rewrite (usefull these days)
    if not files.is_link('/etc/apache2/mods-enabled/rewrite.load'):
        sudo("a2enmod rewrite")   
    
    # apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1 for ServerName
    require.files.file('/etc/apache2/httpd.conf', 
        source='./fabric/files/apache/httpd.conf',
        owner = 'root',
        group = 'root',
        use_sudo=True
    )
    # sudo("rm -R /var/lock/apache2")
    sudo("chown -R vagrant:vagrant /var/lock/apache2")
    sudo("/etc/init.d/apache2 restart")
    installMySql()

@task
def installMySql():
    # install mysql
    require.mysql.server(password='secret')
    with settings(mysql_user='root', mysql_password='secret'):
        require.mysql.user('dbuser', 'bar')
        require.mysql.database('foo', owner='dbuser')
    configMySqlToAllowOutsideConnection()

@task
def configMySqlToAllowOutsideConnection():
    comment('/etc/mysql/my.cnf', r'^bind-address', use_sudo=True)
    mysql.query("GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'secret';",mysql_user='root', mysql_password='secret')
    sudo("service mysql restart")