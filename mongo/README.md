# A Mongodb Vagrant Box

This is a Vagrant configuration for a Mongodb box with essential tools.
The operating system is a Ubuntu 12.04 precise `64` image.

## Requirements

Obviously... [Vagrant](http://www.vagrantup.com/) and [Oracle VirtualBox](https://www.virtualbox.org/).

You will need the awesome [Fabric](http://fabfile.org) and 
[Fabtools](http://fabtools.readthedocs.org) to provision the box:

    pip install fabric
    pip install fabtools

## Running the box

You can start the box using the usual Vagrant `up` command:

    vagrant up

The next steps are obviously to provision it with Fabric, then log in:

    fab vagrant provision
    vagrant ssh

### Mongodb support

The box can be provisioned with [Mongodb](http://mongodb.org/):

    fab vagrant installMongo

Mongodb is installed in `~/?` with the following configuration:

- access to the HTTP interface from the host on port `27017`