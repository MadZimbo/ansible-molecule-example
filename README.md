## Testing Ansible with Molecule 

This repository is an example of how to test Ansible roles with Molecule
You will find a couple of ansible roles that are already initialized with molecule and are ready for experimenting.
Not all molecule features are covered with this example project but you will be able to test your role 
against different OS versions and see the Unit tests in action. 

The role `ossec` provides you with two example molecule.yml files one for a docker driver 
and a second one (molecule.yml.vagrant) for testing against a vagrant box.
Just rename them to activate your desired configuration. By default the docker version is active.  

## Prerequisites  
To use this repo on your local machine you need the following environment 
* Python incl. pip
* Ansible 
* Docker
* Vagrant

Install the following python modules with pip
```sh 
pip install molecule docker python-vagrant
````

## TL;DR - Molecule in Action
Clone the repo 
```sh
git clone git@github.com:MadZimbo/ansible-molecule-example.git  && cd ansible-molecule-example.git 
````
cd into a role, for example check_mk
```sh
cd roles/check_mk
````
Run molecule 
```sh
molecule test
````

# Molecule 

Molecule is a testing framework for Ansible that helps you to write 
better playbooks. 

Molecule has different ways of helping you to write the best playbooks in the world

* Syntax checking for your yaml files and Ansible code
* Initialize new roles and generate the directory layout
* Test your playbooks against different OS versions 
* Test different Ansible versions 
* Unit testing 

# HowTo 

## Create a new role or 'moleculeize' an existing role

Create a new Ansible role with molecule 
```sh
molecule init role --role-name foo
```
Will create a new role directory layout for the role foo

If you already have a role, you can add a molecule scenario with  
```sh
cd foo ; molecule init scenario  --role-name foo
```

In both cases you will find a directory `molecule` where the configuration for your role resides

## Molecule Configuration
The interesting part happens in 
`<yourRole>/molecule/default/tests/molecule.yml`

Here you can define which platform driver to use for example docker or vagrant. 
There are a lot of other drivers available like EC2, GCE, LXE, Azure...
Example:

```sh
driver:
  name: docker
```

You can configure against which OS versions you want to test 
```sh
platforms:
  - name: Ubuntu-Latest
    image: ubuntu:latest
  - name: CentOS-7
    image: centos:7
```

You can define which steps to execute in your testplan when executing 

```sh
molecule test
```

By default molecule would run all steps  
```sh
└── default
    ├── lint
    ├── destroy
    ├── dependency
    ├── syntax
    ├── create
    ├── prepare
    ├── converge
    ├── idempotence
    ├── side_effect
    ├── verify
    └── destroy
```
If you want to skip, lets say the idempotence test change the molecule.yml part to 
```sh
scenario:
  name: default
  test_sequence:
    - lint
    - destroy
    - dependency
    - syntax
    - create
    - prepare
    - converge
    - side_effect
    - verify
    - destroy
```

Molecule would then skip the idempotence task and does not try to discover 
if a playbook is idempotent 


## Unit Test 

Molecule supports unit testing with testinfra.
When you create or initialize a role with molecule it creates a `tests` directory 
inside the molecule directory of your role. 
A default test is generated as well, check the `test_default.py` file 

You can find more tests in the provided roles, check out the `<role>/molecule/default/tests` directory

Files inside the tests directory that are prefixed with `test_` are considered to be tests and are executed by molecule

#### Runing a unit test 

# Gitlab CI 




# Pitfalls

In most cases you test either against a docker container or a Vagrant box
A Vagrant box is a full Virtual Machine a docker container is just isolation at the OS level. 

This can lead to some "problems" if you test roles that rely on things like a init system 
In a default docker container there is normaly no init system available. 
Tasks that restart a service would fail. You can get around those problems with special docker images that are include a init system 
or you use a vagrant box, which is a complete virtual machine. 

 
