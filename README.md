# stock - quick start

```python
from utils import TradierApi

API_URL = 'sandbox.tradier.com'
API_KEY = '[GET THIS FROM tradier.com]'

api = TradierApi(API_URL, API_KEY)
stock_history = api.get_stock_history('GOOGL', '2015-01-01')
print stock_history
```
