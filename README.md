# Tradingbot
# 💹 Binance Futures Testnet Trading Bot (Web UI)

A simple web-based trading bot that lets you place **market**, **limit**, and **stop-market** orders on the **Binance Futures Testnet** using the official Binance API.

Built with:
- 🔧 Python
- 🖥️ Flask (for the web server)
- 📊 TradingView widget (for live BTCUSDT chart)
- 🗝️ .env for API security

---

## 🚀 Features

- ✅ Place Market, Limit, and Stop-Market Orders
- 🔐 Password-Protected Web Interface
- 📈 View Real-Time BTCUSDT Chart (via TradingView)
- 📉 Displays Current Market Price
- ✅ Clean and Minimal HTML UI
- 🛠️ Easily Extensible

---

## 📁 Project Structure

TadingBot/
│
├── app.py # Flask web server
├── bot.py # BasicBot class using binance-python
├── .env # API credentials (not committed)
├── requirements.txt
├── templates/
│ ├── index.html # Web form for placing trades
│ └── login.html # Login page

---

## ⚙️ Setup Instructions

### 🔐 1. Get Binance Futures Testnet API Keys

1. Go to [Binance Futures Testnet](https://testnet.binancefuture.com/)
2. Log in and go to `API Management`
3. Create a new API key pair

---

### 🧪 2. Clone & Setup the Project

```bash
git clone https://github.com/your-username/TadingBot.git
cd TadingBot
```

Create a .env file and add:
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret

📦 3. Install Dependencies
pip install -r requirements.txt

requirements.txt should include:
flask
python-binance
python-dotenv

▶️ 4. Run the Flask App
python app.py
Go to: http://localhost:5000
🔐 Default password: admin123

🔧 Customize
You can modify:
The login password in app.py
Supported order types
Add order history display or SQLite integration

📸 Screenshot
![image](https://github.com/user-attachments/assets/78624869-4964-44f4-8232-814b52962360)
![image](https://github.com/user-attachments/assets/2839314e-9ddd-4313-9e5b-8e3950fb78e3)

⚠️ Disclaimer
This bot uses the Binance Futures Testnet and does not execute real trades.
Do not use real credentials or funds with this code in production without proper security measures.

🧠 Inspired by
Binance API Docs
python-binance

📃 License
MIT License – use it freely and responsibly.
