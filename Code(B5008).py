import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    birth_date = entry.get()
    try:
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
        today = datetime.today()

        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        if days < 0:
            months -= 1
            days += (datetime(today.year, today.month, 1) - datetime(today.year, today.month - 1, 1)).days

        if months < 0:
            years -= 1
            months += 12

        messagebox.showinfo("Age Calculator", f"🎉 You are {years} years, {months} months, and {days} days old!")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format! Use YYYY-MM-DD")

# GUI setup
root = tk.Tk()
root.title("Age Calculator")

tk.Label(root, text="Enter Birthdate (YYYY-MM-DD):").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Calculate Age", command=calculate_age, background='red',foreground='black' ).pack(pady=15)

root.mainloop()
