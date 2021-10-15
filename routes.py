from flask import current_app as app
from flask import render_template, Response
from flask import request, redirect, url_for
import requests, json
from coinbase.wallet.client import Client

@app.route('/')
def home():
    return "Home"

@app.route('/prices/')
def display_prices():
    p1 = coinbase_prices()
    p2 = gemini_prices()
    #print(p1, p2)
    data = [p2[0], p2[1], p1[0]['amount'], p1[1]['amount']]
    data2 = [p2[2], p2[3], p1[2]['amount'], p1[3]['amount']]
    return render_template('prices.html', data=data, data2=data2)
    return p1, p2
    return "Prices"

def coinbase_prices():

	#client = Client('qgtZ6JlI71SfrPei', 'D45Zc88V8xIkWnx7Di6PGMpkFF163JMf')
        coinbase_api_key = app.config['coinbase_api_key']
        coinbase_secret_key = app.config['coinbase_secret_key']
        client = Client(coinbase_api_key, coinbase_secret_key)

	bitcoin_buy_price = client.get_buy_price(currency_pair = 'BTC-USD')
	bitcoin_sell_price = client.get_sell_price(currency_pair = 'BTC-USD')

	eth_buy_price = client.get_buy_price(currency_pair = 'ETH-USD')
	eth_sell_price = client.get_sell_price(currency_pair = 'ETH-USD')

	return bitcoin_buy_price, bitcoin_sell_price, eth_buy_price, eth_sell_price

def gemini_prices():
	base_url = "https://api.gemini.com/v1"
	response1 = requests.get(base_url + "/pubticker/btcusd")
	response2 = requests.get(base_url + "/pubticker/ethusd")

	btc_data = response1.json()
	eth_data = response2.json()

	return btc_data['ask'], btc_data['bid'], eth_data['ask'], eth_data['bid']


# def get_prices():
# 	params = {'access_key': 'd98674ec17a4b1a1b2ee770174c25dcb'}
# 	r = requests.get("http://api.coinlayer.com/live", params=params)
# 	data = r.json()

class EndpointAction(object):

    def __init__(self, action):
        self.action = action
        self.response = Response(status=200, headers={})

    def __call__(self, *args):
        return self.action()
        #return self.response


class FlaskAppWrapper(object):
    #app = None

    def __init__(self, app):
        self.app = app
        #self.app = Flask(name)

    def run(self):
        self.app.run()

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name, EndpointAction(handler))

#a = FlaskAppWrapper(app)
#a.add_endpoint(endpoint='/prices', endpoint_name='prices', handler=display_prices)
#a.run()
