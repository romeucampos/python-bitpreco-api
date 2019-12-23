import pytest


import bitpreco
from bitpreco.erros import ApiError

@pytest.fixture
def bitp():
    return bitpreco.Api("key",
                        "secret")



def test_balance(bitp):
    response = bitp.balance()
    assert dict == type(response)
    assert 'success' in response
    assert 'BTC' in response
    assert 'BTC_locked' in response
    assert 'BRL' in response
    assert 'BRL_locked' in response


def test_buy_minium_amount(bitp):
    with pytest.raises(ApiError) as e:
        response = bitp.buy(0, 0)

    assert 'Invalid response: BELOW_MINIMUM_AMOUNT' in str(e.value)
    

def test_buy_max_amount(bitp):
    with pytest.raises(ApiError) as e:
        response = bitp.buy(100000000, 100000000)

    assert 'Invalid response: ABOVE_MAX_AMOUNT' in str(e.value)


def test_open_orders(bitp):
    response = bitp.open_orders()
    assert [] == response
    
