import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_installed_packages(host):
    assert host.package("zookeeper").is_installed
    assert host.package("zookeeper-bin").is_installed
    assert host.package("zookeeperd").is_installed

def test_zookeeper_running_and_enabled(host):
    service = host.service("zookeeper")
    assert service.is_running
    assert service.is_enabled

def test_myid(host):
    ansible_vars = host.ansible.get_variables()
    dataDir_path = ansible_vars["zookeeper_dataDir"]
    myid_path = dataDir_path + "/myid"
    assert host.file(myid_path).exists
    assert host.file(myid_path).is_file

    zookeeper_server_ips = host.ansible("debug", "msg={{ zookeeper_server_ips }}")["msg"]
    myid = zookeeper_server_ips.index(ansible_vars["local_ipv4"]) + 1
    myid_from_host = host.file(myid_path).content_string
    assert str(myid) == myid_from_host[:-1]
