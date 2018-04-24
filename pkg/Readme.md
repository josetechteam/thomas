# installing packages on linux for josetechteam


## Ruby is installed by default - yay!

## Installing iruby for jupyter notebooks - hard!

### Install zeromq

1. ./zeromq_setup.sh
2. the above installs build-essential -- and other packages needed at the library level
3. zero mq is a message queueing system - a study in itself - not germane here.

#### Reference
- https://gist.github.com/katopz/8b766a5cb0ca96c816658e9407e83d00
- https://en.wikipedia.org/wiki/ZeroMQ


### Install jupiter notebook

- pip3 install --upgrade pip
- pip3 install jupyter

### Install iruby - hard!

#### Centos notes
- http://devopspy.com/linux/ruby-kernel-jupyter-notebook/



- pip3 install ipython==5.0.0
- pip3 install jupyter


#### Rewrite this for ubuntu - perhaps not needed after zeromq installs many of these things
- sudo yum install -y git-core ruby-devel ruby zlib zlib-devel gcc-c++ patch readline readline-devel libyaml-devel libffi-devel openssl-devel make



- sudo yum install zeromq-devel zeromq czmq
- gem install cztop rbczmq ffi_rzmq
- gem install iruby

- iruby register --force


## additional info
I needed to install ruby-dev:

sudo apt-get install ruby-dev zlib1g-dev liblzma-dev



