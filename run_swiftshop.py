import subprocess

# Run object detection
subprocess.Popen(["python", "scripts/object_detection.py"])

# Run Telegram bot
subprocess.Popen(["python", "scripts/telegram_bot.py"])

# Run OLED Display (on Raspberry Pi)
subprocess.Popen(["python", "raspberry_pi/oled_display.py"])
