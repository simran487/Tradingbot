from bot import BasicBot
from utils import save_order_to_csv
from dotenv import load_dotenv
import os

print("=== Binance Futures Testnet Trading Bot ===")

# Load API key and secret from .env file
load_dotenv()
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

# Create bot instance
bot = BasicBot(api_key, api_secret)

symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
side = input("Enter side (buy/sell): ").lower()
order_type = input("Enter order type (market/limit/stop-market): ").lower()
quantity = float(input("Enter quantity: "))


# Get current market price and show it
price_data = bot.client.futures_symbol_ticker(symbol=symbol)
current_price = float(price_data["price"])
print(f"Current Market Price for {symbol}: {current_price}")


price = None
stop_price = None

if order_type == "limit":
    price = float(input("Enter limit price: "))
elif order_type == "stop-market":
    stop_price = float(input("Stop price: "))

# Map string to Binance constant
order_type_map = {
    "market": "MARKET",
    "limit": "LIMIT",
    "stop-market": "STOP_MARKET"
}


# Place order
order = bot.place_order(
    symbol=symbol,
    side=side,
    quantity=quantity,
    order_type=order_type_map[order_type],
    price=price,
    stop_price=stop_price
)

print("Order Response:", order)


# Save order to CSV if successful
if 'status' in order:
    save_order_to_csv(order)



print("\nWhat would you like to do next?")
print("1. View open orders")
print("2. Cancel an order")
print("3. View order history")
print("4. Exit")

choice = input("Enter choice (1-4): ")

if choice == "1":
    open_orders = bot.get_open_orders(symbol)
    print("Open Orders:", open_orders)

elif choice == "2":
    cancel_id = input("Enter Order ID to cancel: ")
    cancel_result = bot.cancel_order(symbol, int(cancel_id))
    print("Cancel Result:", cancel_result)

elif choice == "3":
    history = bot.get_order_history(symbol)
    print("Order History:", history)
