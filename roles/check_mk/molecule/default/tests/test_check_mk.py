def test_check_mk_version(host):
    assert host.check_output(
        'check_mk_agent|head -2|grep Version') == "Version: 1.2.8p26"


def test_check_mk_file(host):
    f = host.file('/etc/xinetd.d/check_mk')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
