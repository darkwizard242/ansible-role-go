import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_go_source_exists(host):
    assert host.file('/usr/local/go').exists


def test_go_source_isdirectory(host):
    assert host.file('/usr/local/go').is_directory


def test_go_binary_exists(host):
    assert host.file('/usr/local/go/bin/go').exists


def test_go_binary_file(host):
    assert host.file('/usr/local/go/bin/go').is_file


def test_go_export_file_exists(host):
    assert host.file('/etc/profile.d/go.sh').exists


def test_go_export_file_isfile(host):
    assert host.file('/etc/profile.d/go.sh').is_file
