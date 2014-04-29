# Fabtool Vagrant Boxes

This is a Vagrant configuration for a given box with essential tools.
The operating system is a Ubuntu 12.04 precise `x64` image.
Default vagrant VM box configuration takes 384 Mb of Ram and 2 cpu cores.
Storage space is (as I suppose) adequate to you disk space or something.

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