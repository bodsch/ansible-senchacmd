import pytest
import os
import yaml
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def get_vars(host):
    defaults_files = "file=../../defaults/main.yml name=role_defaults"
    vars_files = "file=../../vars/main.yml name=role_vars"

    ansible_vars = host.ansible(
        "include_vars",
        defaults_files)["ansible_facts"]["role_defaults"]

    ansible_vars.update(host.ansible(
        "include_vars",
        vars_files)["ansible_facts"]["role_vars"])

    # print(ansible_vars)

    return ansible_vars


@pytest.mark.parametrize("dirs", [
    "/opt/Sencha/Cmd"
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/etc/profile.d/sencha.sh",
    "/opt/Sencha/Cmd/sencha",
    "/opt/Sencha/Cmd/version.properties",
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file

def test_installation_directory(host, get_vars):
    vers = get_vars['sencha_version']

    directory = "/opt/Sencha/Cmd/{}".format(vers)

    d = host.file(directory)
    assert d.is_directory
    assert d.exists

    for file in ["sencha.jar","sencha.vmoptions"]:
        f = host.file("{}/{}".format(directory, file))
        assert f.exists
        assert f.is_file

