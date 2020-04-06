[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-go.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-go) ![Ansible Role](https://img.shields.io/ansible/role/47668?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/47668?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/47668?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-go&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-go) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-go?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-go?color=orange&style=flat-square)

# Ansible Role: go

Role to install (_by default_) [go](https://golang.org) programming language on **Debian/Ubuntu** and **EL** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
go_app: go
go_version: 1.14.1
go_osarch: linux-amd64
go_dl_url: "https://dl.google.com/{{ go_app }}/{{ go_app }}{{ go_version }}.{{ go_osarch }}.tar.gz"
go_bin_path: /usr/local
go_profile_template_export_line: "{{ go_bin_path}}/go/bin"
go_profile_template_path: /etc/profile.d
go_profile_template_source_file: go.j2
go_profile_template_dest_file: go.sh
```

### Variables table:

Variable                        | Value (default)                                                                            | Description
------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------
go_app                          | go                                                                                         | Defines the app to install i.e. **go**
go_version                      | 1.14.1                                                                                     | Defined to dynamically fetch the desired version to install. Defaults to: **1.14.1**
go_osarch                       | linux-amd64                                                                                | Defines os architecture. Used for obtaining the correct type of binaries based on OS System Architecture. Defaults to: **linux-amd64**
go_dl_url                       | "<https://dl.google.com/{{> go_app }}/{{ go_app }}{{ go_version }}.{{ go_osarch }}.tar.gz" | Defines URL to download the go binary from.
go_bin_path                     | /usr/local                                                                                 | Defined to dynamically set the appropriate path to store go binary into. Defaults to: **/usr/local** - which is sourced using a handler.
go_profile_template_export_line | "{{ go_bin_path}}/go/bin"                                                                  | Defined to set the line for export to path within a custom file generated into /etc/profile.d directory.
go_profile_template_path        | /etc/profile.d                                                                             | Directory in which to generate go's PATH export template to.
go_profile_template_source_file | go.j2                                                                                      | Source template file for export of go's binary into PATH.
go_profile_template_dest_file   | go.sh                                                                                      | Destination filename that will be placed in /etc/profile.d with go's PATH export as.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **go**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.go
```

For customizing behavior of role (i.e. specifying the desired **go** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.go
  vars:
    go_version: 1.14.0
```

For customizing behavior of role (i.e. placing binary of **go** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.go
  vars:
    go_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-go/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
