def test_curl_is_installed(host):
    curl = host.package("curl")
    assert curl.is_installed
