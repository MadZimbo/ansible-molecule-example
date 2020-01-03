def test_for_ossec_monitor_daemon(host):
    host.process.get(comm="ossec-monitord")


def test_for_ossec_syscheck_daemon(host):
    host.process.get(comm="ossec-syscheckd")
