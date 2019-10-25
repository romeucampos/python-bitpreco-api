# python bitpreco api

A Python wrapper for Bitpreço API. 
Forked project from python-bitcointrade-api by Leandro Trindade (just4span@gmail.com)

## Installation


```bash
pip install git+https://github.com/romeucampos/python-bitpreco-api.git
```

You can also install directly from the GitHub repository to have the newest features by running:

```bash
git clone https://github.com/romeucampos/python-bitpreco-api.git
cd python-bitpreco-api
python setup.py install
```

## Basic Usage

Below you can see the available Bitpreco API methods you can use:

```python
import bitpreco
bitp = bitpreco.Api()

bitp.ticker()
bitp.orderbook()
bitp.trades()
bitp.exchanges()
```

And the methods private Trade API:

```python
import bitpreco
bitp = bitpreco.Api("<api_key>", "<signature>")

bitp.balance()
bitp.open_orders()
bitp.buy(price=30200, amount=0.01)
bitp.sell(price=30100, amount=0.01)
bitp.all_orders_cancel()
bitp.order_cancel(order_id="<order_id>")
bitp.order_status(order_id="<order_id>")
```


## References

[Bitpreço API](https://bitpreco.com/api.html)
