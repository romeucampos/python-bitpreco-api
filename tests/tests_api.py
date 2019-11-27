import unittest

import bitpreco


class ApiTest(unittest.TestCase):
    def setUp(self):
        self.bitp = bitpreco.Api()

    def test_ticker(self):
        response = self.bitp.ticker()
        assert type(response) == dict
        assert 'last' in response
        assert 'high' in response
        assert 'low' in response
        assert 'vol' in response
        assert 'var' in response
        assert 'timestamp' in response
    
    def test_orderbook(self):
        response = self.bitp.orderbook()
        assert type(response) == dict
        assert 'bids' in response
        assert 'asks' in response
        assert 'timestamp' in response

    def test_trades(self):
        response = self.bitp.trades()
        assert type(response) == list
        assert 'type' in response[0]
        assert 'amount' in response[0]
        assert 'timestamp' in response[0]
        assert 'price' in response[0]
    
    def test_exchanges(self):
        response = self.bitp.exchanges()
        assert type(response) == list
        assert 'name' in response[0]
        assert 'execution' in response[0]
        assert 'deposit' in response[0]
        assert 'withdrawal' in response[0]
        assert 'bid' in response[0]
        assert 'ask' in response[0]
        assert 'timestamp' in response[0]
        

if __name__ == '__main__':
    unittest.main()
