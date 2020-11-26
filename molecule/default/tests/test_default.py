import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE_SOURCE = '/usr/local/go'
PACKAGE_BINARY = '/usr/local/go/bin/go'
PACKAGE_PROFILE_LOAD = '/etc/profile.d/go.sh'


def test_go_source_exists(host):
    """
    Tests if go source exists.
    """
    assert host.file(PACKAGE_SOURCE).exists


def test_go_source_isdirectory(host):
    """
    Tests if go source is directory type.
    """
    assert host.file(PACKAGE_SOURCE).is_directory


def test_go_binary_exists(host):
    """
    Tests if go binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_go_binary_file(host):
    """
    Tests if go binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_go_export_file_exists(host):
    """
    Tests if a profile file exists for loading go.
    """
    assert host.file(PACKAGE_PROFILE_LOAD).exists


def test_go_export_file_isfile(host):
    """
    Tests if profile file for loading go is file type.
    """
    assert host.file(PACKAGE_PROFILE_LOAD).is_file
