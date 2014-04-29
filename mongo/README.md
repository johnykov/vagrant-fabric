# A Mongodb Vagrant Box

### Mongodb support

The box can be provisioned with [Mongodb](http://mongodb.org/):

    fab vagrant installMongo

Mongodb is installed in `~/?` with the following configuration:

- access to the HTTP interface from the host on port `27017`

This is very handful for developing apps with [mean.io](http://mean.io/) stack.
