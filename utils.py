import httplib
import json

class TradierApi(object):
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def get_stock_history(self, symbol, start):
        """
        symbol: string
        start: string (YYYY-MM-DD)
        """
        connection = httplib.HTTPSConnection(self.api_url, 443, timeout = 30)

        # Headers
        headers = {"Accept":"application/json",
                   "Authorization":"Bearer {0}".format(self.api_key)}

        # Send synchronously
        connection.request('GET', '/v1/markets/history?symbol={symbol}&interval=daily&start={start}'.format(symbol=symbol,start=start), None, headers)
        try:
          response = connection.getresponse()
          return json.loads(response.read())['history']['day']

        except httplib.HTTPException, e:
          # Exception
          print('Exception during request')
