from flask import Flask, render_template, request, redirect, url_for, session
from bot import BasicBot
from dotenv import load_dotenv
import os

# Load API keys
load_dotenv()
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

# Flask setup
app = Flask(__name__)
app.secret_key = "super_secret_key"  # 🔐 Change this to a strong secret key

# Create bot instance
bot = BasicBot(api_key, api_secret)

# 🔐 Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == "admin123":  # 🧾 You can change this password
            session['authenticated'] = True
            return redirect(url_for('index'))
        else:
            return "❌ Incorrect password. Try again."
    return render_template('login.html')


# 💻 Main Page: Order Placement + Market Price
@app.route('/', methods=['GET', 'POST'])
def index():
    if not session.get('authenticated'):
        return redirect(url_for('login'))

    order_response = None
    market_price = None

    if request.method == 'POST':
        symbol = request.form['symbol'].upper()
        side = request.form['side'].lower()
        order_type = request.form['order_type'].lower()
        quantity = float(request.form['quantity'])

        price = request.form.get('price')
        stop_price = request.form.get('stop_price')

        # ✅ Get current market price
        try:
            price_data = bot.client.futures_symbol_ticker(symbol=symbol)
            market_price = float(price_data["price"])
        except:
            market_price = "Error fetching price"

        # 🧭 Map order type
        order_type_map = {
            "market": "MARKET",
            "limit": "LIMIT",
            "stop-market": "STOP_MARKET"
        }

        # ✅ Place order
        order_response = bot.place_order(
            symbol=symbol,
            side=side,
            quantity=quantity,
            order_type=order_type_map[order_type],
            price=float(price) if price else None,
            stop_price=float(stop_price) if stop_price else None
        )

    return render_template('index.html', response=order_response, market_price=market_price)

if __name__ == '__main__':
    app.run(debug=True)
