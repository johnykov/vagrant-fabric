# A Apache Tomcat Vagrant Box

### Tomcat support

The box can be provisioned with [Tomcat](http://tomcat.apache.org/):

    fab vagrant provision

Tomcat is installed in `/usr/share/tomcat` with the following configuration:

- access to the HTTP interface from the host on port `8080`

## App deployment on tomcat
  
You can deploy a sample app to your new tomcat instance

    fab vagrant deploySample