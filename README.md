# Ansible Module demo
This is a demo of how to write your own Ansible module.

## DIY
 1. Create a project directory:
    1. E.g. `mkdir ansible-hello-module && cd $_`
 2. Create a directory for the Python module code, logs and tasks:
    1. E.g. `mkdir logs modules tasks`
 3. Create a README file, .gitignore and ansible.cfg:
    1. `touch .gitignore README.md ansible.cfg`

What files should be ignored? Sensitive files, logs, etc. and non-essential files. Files that are added by any install command, too.
A starting point might be: [How to ignore files in Git.](https://linuxize.com/post/gitignore-ignoring-files-in-git/)

```bash
> cat .gitignore
.idea/
env/
logs/
*.log
```

```ini
> cat ansible.cfg
[defaults]
library = modules/
log_path = logs/ansible.log
deprecation_warnings = False
host_key_checking = false
```
Ansible will look for the module in the `modules` directory. But it can be named differently, of course. Just remember to change the `library` setting in the `ansible.cfg` file accordingly.

## Setup the Python environment

Make sure you have Python 3 (latest is always good) installed and that pip is up to date.

```bash
> python3 -V
> pip install --upgrade pip
> python3 -m venv env && source env/bin/activate
> pip install ansible
Collecting ansible
  Downloading ansible-5.2.0.tar.gz (37.9 MB)
     |████████████████████████████████| 37.9 MB 5.1 MB/s
Collecting ansible-core~=2.12.1
  Downloading ansible-core-2.12.1.tar.gz (7.4 MB)
     |████████████████████████████████| 7.4 MB 4.1 MB/s
     ...
```

After the Python environment is set up, you can start coding your module. This example project contains a Python module called `calculate.py`. 

Nota bene: The name of the module is important. It is used to import the module in the `tasks` directory. 
In the file `tasks/demo.yml` you can see how to use the module `calculate.py` - it is called in the task with `calculate:`.

```yaml
---
- name: Test calculate module
  hosts: localhost
  connection: local
  gather_facts: false

  tasks:
    - name: Add two numbers
      calculate:
        method: add
        number1: 4
        number2: 7
      register: result
    - debug:
        msg: "Add 4+7 => {{ result.msg }}"
```

