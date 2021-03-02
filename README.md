
The role installs [SenchaCmd](https://www.sencha.com/products/sencha-cmd/).


[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/bodsch/ansible-senchacmd/CI)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-senchacmd)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-senchacmd)][releases]

[ci]: https://github.com/bodsch/ansible-senchacmd/actions
[issues]: https://github.com/bodsch/ansible-senchacmd/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-senchacmd/releases


## Example Playbook

```
 - hosts: all
   roles:
     - role: sencha_cmd
```

## Role Variables

[defaults/main.yml](defaults/main.yml)

| *Variable*                  | *Default Value*   | *Description* |
| :---                        | :---              | :--- |
| `sencha_cleanup`            | `false`           | clean temporary directory after installation  |
| `sencha_version`            | `6.5.3.6`         | Version number |
| `sencha_home_directory`     | `/opt/Sencha/Cmd` | SENCHA_HOME parent directory |
| `sencha_memory.max_heap`    | `4G`              | specify the maximum heap size |
| `sencha_memory.inital_heap` | `512m`            | specify the initial Java heap size |


## Tests

```
$ tox -e py38-ansible29 -- molecule test -s default
```
