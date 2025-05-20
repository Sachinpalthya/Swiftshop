from telegram import Bot
import firebase_admin
from firebase_admin import credentials, db

# Firebase setup
cred = credentials.Certificate("firebase/firebase_credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://your-database-url.firebaseio.com"})

# Telegram bot setup
bot = Bot(token="YOUR_TELEGRAM_BOT_TOKEN")
chat_id = "CUSTOMER_CHAT_ID"

# Fetch bill from Firebase
ref = db.reference("billing")
bill_data = ref.get() or {}

bill_message = "\n".join([f"{p}: {d['quantity']} x Rs{d['price']}" for p, d in bill_data.items()])
total_bill = sum(d["price"] * d["quantity"] for d in bill_data.values())

bot.send_message(chat_id, f"Your Swiftshop Bill:\n{bill_message}\nTotal: Rs {total_bill}\nPay here: [Payment Link]")

