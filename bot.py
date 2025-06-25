from binance.client import Client
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
            self.client.API_URL = 'https://testnet.binancefuture.com'

    def place_order(self, symbol, side, quantity, order_type="MARKET", price=None, stop_price=None):
        try:
            params = {
                'symbol': symbol,
                'side': 'BUY' if side.lower() == 'buy' else 'SELL',
                'type': order_type,
                'quantity': quantity
            }

            if order_type == "LIMIT":
                if not price:
                    raise ValueError("Price must be specified for limit orders.")
                params['price'] = price
                params['timeInForce'] = "GTC"

            elif order_type == "STOP_MARKET":
                if not stop_price:
                    raise ValueError("Stop price must be specified for stop-market orders.")
                params['stopPrice'] = stop_price
                params['timeInForce'] = "GTC"

            order = self.client.futures_create_order(**params)
            logging.info(f"Order placed: {order}")
            return order

        except Exception as e:
            logging.error(f"Order failed: {e}")
            return {'error': str(e)}


    def get_open_orders(self, symbol=None):
        try:
            orders = self.client.futures_get_open_orders(symbol=symbol) if symbol else self.client.futures_get_open_orders()
            return orders
        except Exception as e:
            return {"error": str(e)}


    def cancel_order(self, symbol, order_id):
        try:
            result = self.client.futures_cancel_order(symbol=symbol, orderId=order_id)
            return result
        except Exception as e:
            return {"error": str(e)}

    def get_order_history(self, symbol):
        try:
            return self.client.futures_get_all_orders(symbol=symbol)
        except Exception as e:
            return {"error": str(e)}

