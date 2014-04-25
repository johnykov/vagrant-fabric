# A LAMP Vagrant Box

This is a Vagrant configuration for a LAMP (linux, apache, mysql, php) box with essential tools.
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

    fab vagrant install
    vagrant ssh


This are modified files from [here](http://www.k3z.fr/blog/post/3/Developpement_Vagrant_debian_fabric_trio_gagnant)