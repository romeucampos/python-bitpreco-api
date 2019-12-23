import pytest

import bitpreco


@pytest.fixture
def bitp():
    return bitpreco.Api()


def test_ticker(bitp):
    response = bitp.ticker()
    assert type(response) == dict
    assert 'last' in response
    assert 'high' in response
    assert 'low' in response
    assert 'vol' in response
    assert 'var' in response
    assert 'timestamp' in response


def test_orderbook(bitp) :
    response = bitp.orderbook()
    assert type(response) == dict
    assert 'bids' in response
    assert 'asks' in response
    assert 'timestamp' in response


def test_trades(bitp):
    response = bitp.trades()
    assert type(response) == list
    
    for rsp in response:
        assert 'type' in rsp
        assert 'amount' in rsp
        assert 'timestamp' in rsp
        assert 'price' in rsp


def test_exchanges(bitp):
    response = bitp.exchanges()
    assert type(response) == list
    
    for rsp in response:
        assert 'name' in rsp
        assert 'execution' in rsp
        assert 'deposit' in rsp
        assert 'withdrawal' in rsp
        assert 'bid' in rsp
        assert 'ask' in rsp
        assert 'timestamp' in rsp
