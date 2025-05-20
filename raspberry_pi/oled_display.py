import board
import busio
import adafruit_ssd1306
import firebase_admin
from firebase_admin import credentials, db

# Firebase setup
cred = credentials.Certificate("firebase/firebase_credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://your-database-url.firebaseio.com"})

# OLED setup
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

while True:
    ref = db.reference("billing")
    bill_data = ref.get() or {}

    total_bill = sum(item["price"] * item["quantity"] for item in bill_data.values())

    oled.fill(0)
    oled.text(f"Total: Rs {total_bill}", 0, 10, 1)
    oled.show()

