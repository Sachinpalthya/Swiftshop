import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Swiftshop - Smart Billing")
        self.root.geometry("400x500")
        
        self.items = {}  # item_name: count
        self.prices = {
            "Bottle": 20,
            "Person": 0,
            "Pepsi": 40,
            "Appy": 35,
            # Add more as needed
        }

        self.bill_frame = tk.Frame(root)
        self.bill_frame.pack(pady=10)

        self.bill_text = tk.Text(self.bill_frame, height=20, width=40)
        self.bill_text.pack()

        self.total_label = tk.Label(root, text="Total: ₹0", font=("Arial", 14))
        self.total_label.pack()

        self.btn_save = tk.Button(root, text="🧾 Save Bill", command=self.save_bill)
        self.btn_save.pack(pady=5)

    def add_item(self, item_name):
        if item_name in self.prices:
            self.items[item_name] = self.items.get(item_name, 0) + 1
            self.update_bill()

    def update_bill(self):
        self.bill_text.delete("1.0", tk.END)
        total = 0
        for item, qty in self.items.items():
            price = self.prices[item] * qty
            self.bill_text.insert(tk.END, f"{item} x {qty} = ₹{price}\n")
            total += price
        self.total_label.config(text=f"Total: ₹{total}")

    def save_bill(self):
        now = datetime.now().strftime("%Y%m%d_%H%M%S")  # ✅ Define here
        with open(f"bill_{now}.txt", "w", encoding="utf-8") as f:
            f.write(self.bill_text.get("1.0", tk.END))
            f.write(f"\n{self.total_label.cget('text')}")
        messagebox.showinfo("Saved", "Bill saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BillingApp(root)

    # Simulate adding detected items (for testing)
    app.add_item("Bottle")
    app.add_item("Pepsi")

    root.mainloop()
