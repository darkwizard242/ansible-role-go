[[![build-test](https://github.com/darkwizard242/ansible-role-go/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-go/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-go/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-go/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/go) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-go&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-go) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-go&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-go) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-go&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-go) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-go?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-go?color=orange&style=flat-square)

# Ansible Role: go

Role to install (_by default_) [go](https://golang.org) programming language on **Debian/Ubuntu** and **EL** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
go_app: go
go_setup: true
go_version: 1.22.4
go_os: "{{ ansible_system | lower }}"
go_architecture_map:
  amd64: amd64
  arm: arm64
  x86_64: amd64
  armv6l: armv6
  armv7l: armv7
  aarch64: arm64
  32-bit: "386"
  64-bit: amd64
go_dl_url: "https://dl.google.com/{{ go_app }}/{{ go_app }}{{ go_version }}.{{ go_os }}-{{ go_architecture_map[ansible_architecture] }}.tar.gz"
go_bin_path: /usr/local
go_profile_template_export_line: "{{ go_bin_path}}/go/bin"
go_profile_template_path: /etc/profile.d
go_profile_template_source_file: go.j2
go_profile_template_dest_file: go.sh
```

### Variables table:

Variable                        | Description
------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
go_app                          | Defines the app to install i.e. **go**
go_setup                        | Boolean variable that only allows `true` or `false` values. Defaults to `true`. When set to `true` it will setup/install go. When set to `false`, it will remove go from the system - assuming it was installed via this role and value for `go_bin_path` path is correct.
go_version                      | Defined to dynamically fetch the desired version to install. Defaults to: **1.22.4**
go_os                           | Defines OS type. Used for obtaining the correct type of binaries based on OS.
go_architecture_map             | Defines Architecture type. Used for obtaining the correct type of binaries based on Architecture.
go_dl_url                       | Defines URL to download the go binary from.
go_bin_path                     | Defined to dynamically set the appropriate path to store go binary into. Defaults to: **/usr/local** - which is sourced using a handler.
go_profile_template_export_line | Defined to set the line for export to path within a custom file generated into /etc/profile.d directory.
go_profile_template_path        | Directory in which to generate go's PATH export template to.
go_profile_template_source_file | Source template file for export of go's binary into PATH.
go_profile_template_dest_file   | Destination filename that will be placed in /etc/profile.d with go's PATH export as.

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
    go_setup: true
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

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
