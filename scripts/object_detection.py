import cv2
from ultralytics import YOLO
import firebase_admin
from firebase_admin import credentials, db

# Load YOLO model
model = YOLO("models/best.pt")  # Trained YOLOv8 model

# Firebase setup
cred = credentials.Certificate("firebase/firebase_credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://your-database-url.firebaseio.com"})

def update_firebase(product, price):
    ref = db.reference("billing")
    bill_data = ref.get() or {}

    if product in bill_data:
        bill_data[product]["quantity"] += 1
    else:
        bill_data[product] = {"price": price, "quantity": 1}

    ref.set(bill_data)  # Update database

# Start Camera
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    for result in results:
        for box in result.boxes:
            label = model.names[int(box.cls[0])]
            update_firebase(label, 50)  # Example price

    cv2.imshow("Swiftshop Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
