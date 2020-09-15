# ansible role for SenchaCmd

The role installs SenchaCmd.

## Example Playbook

```
 - hosts: all
   roles:
     - role: sencha_cmd
```

## Role Variables

[defaults/main.yml](defaults/main.yml)

|*Variable*  | *Default Value* | *Description* |
| --- | --- | --- |
| `sencha_cleanup` | `false` | clean temporary directory after installation  |
| `sencha_version` | `6.5.3.6` | Version number |
| `sencha_home_directory` | `/opt/Sencha/Cmd` | SENCHA_HOME parent directory |
| `sencha_memory_max_heap` | `4G` | specify the maximum heap size |
| `sencha_memory_inital_heap` | `512m` | specify the initial Java heap size |


## Tests

```
$ tox -e py37-ansible29 -- molecule test -s default
```
