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
    coinbase_prices = get_coinbase_prices()
    gemini_prices = get_gemini_prices() 
    
    if not coinbase_prices or not gemini_prices:
        return render_template('500.html'), 500 

    coinbase_btc_buy_price, coinbase_btc_sell_price, coinbase_eth_buy_price, coinbase_eth_sell_price = coinbase_prices
    gemini_btc_buy_price, gemini_btc_sell_price, gemini_eth_buy_price, gemini_eth_sell_price = gemini_prices

    btc_prices = [coinbase_btc_buy_price, gemini_btc_buy_price, coinbase_btc_sell_price, gemini_btc_sell_price]
    eth_prices = [coinbase_eth_buy_price, gemini_eth_buy_price, coinbase_eth_sell_price, gemini_eth_sell_price]

    if coinbase_btc_buy_price > gemini_btc_buy_price:
        btc_buy_reco = "Gemini"
    else:
        btc_buy_reco = "Coinbase"

    if coinbase_btc_sell_price > gemini_btc_sell_price:
        btc_sell_reco = "Coinbase"
    else:
        btc_sell_reco = "Gemini"

    if coinbase_eth_buy_price > gemini_eth_buy_price:
        eth_buy_reco = "Gemini"
    else:
        eth_buy_reco = "Coinbase"

    if coinbase_eth_sell_price > gemini_eth_sell_price:
        eth_sell_reco = "Coinbase"
    else:
        eth_sell_reco = "Gemini"

    return render_template('prices.html', eth_prices=eth_prices,
                           btc_prices=btc_prices, btc_buy_reco=btc_buy_reco,
                           btc_sell_reco=btc_sell_reco,
                           eth_buy_reco=eth_buy_reco, eth_sell_reco=eth_sell_reco)

def get_coinbase_prices():
        coinbase_api_key = app.config['coinbase_api_key']
        coinbase_secret_key = app.config['coinbase_secret_key']

        try:
            client = Client(coinbase_api_key, coinbase_secret_key)

            bitcoin_buy_price = client.get_buy_price(currency_pair = 'BTC-USD')['amount']
            bitcoin_sell_price = client.get_sell_price(currency_pair = 'BTC-USD')['amount']

            eth_buy_price = client.get_buy_price(currency_pair = 'ETH-USD')['amount']
            eth_sell_price = client.get_sell_price(currency_pair = 'ETH-USD')['amount']
        except:
            return []

        return bitcoin_buy_price, bitcoin_sell_price, eth_buy_price, eth_sell_price
    
def get_gemini_prices():
        base_url = "https://api.gemini.com/v1"
        response1 = requests.get(base_url + "/pubticker/btcusd")
        response2 = requests.get(base_url + "/pubticker/ethusd")
        
        if response1.status_code != 200 or response2.status_code != 200:
            return []

        btc_data = response1.json()
        eth_data = response2.json()

        if btc_data.get('result', None) or eth_data.get('result', None):
            return []
        
        return btc_data['ask'], btc_data['bid'], eth_data['ask'], eth_data['bid']
