def _test_X(chain, X, args):
    demo, _ = chain.provider.get_or_deploy_contract('FormattingDemo')
    set_fun = getattr(demo.transact(), 'set' + X)
    get_fun = getattr(demo.call(), 'storage' + X)

    for arg in args:
        txhash = set_fun(arg)
        chain.wait.for_receipt(txhash)

        storage = get_fun()
        assert type(storage) == type(arg)
        assert storage == arg
    return


def test_matrix(chain):
    _test_X(chain, 'Bytes', [b'deadbeef'])
    _test_X(chain, 'Bytes20', [b'deadbeefdeadbeefdeadbeefdeadbeefdeadbeef'])
    _test_X(chain, 'Address', ["0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef"])
    _test_X(chain, 'String', ["deadbeef", "0xdeadbeef", "-0xdeadbeef",
                              "tentacle", "0xtentacle", "-0xtentacle"])
    return
