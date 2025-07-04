# time_machine_gui.py
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random
import time
import threading

past_events = [
    "📜 World War I breaks out in Europe.",
    "🇮🇳 India gains independence from British rule.",
    "👨‍🚀 First human lands on the moon.",
    "🌐 Internet becomes publically available.",
    "🤖 AI becomes self-aware briefly."
]

future_events = [
    "🚀 Humans establish colony on Mars.",
    "🌀 Time travel becomes commercial.",
    "🧠 AI runs most governments.",
    "🌌 Earth joins Galactic Federation.",
    "🦖 Dinosaurs revived through cloning."
]

def get_event(date_input):
    try:
        today = datetime.now()
        input_date = datetime.strptime(date_input, "%Y-%m-%d")

        if input_date < today:
            return random.choice(past_events)
        else:
            return random.choice(future_events)
    except ValueError:
        return None

def simulate_time_travel(entry, label):
    date_input = entry.get()
    label.config(text="⏳ Time Travel Initializing...")

    def run_sequence():
        time.sleep(1)
        for i in range(3):
            label.config(text="⏳ Jumping" + "." * (i + 1))
            time.sleep(0.6)

        event = get_event(date_input)
        if event:
            label.config(text=f"🗓️ Date: {date_input}\n✨ {event}")
        else:
            label.config(text="❌ Invalid date. Use YYYY-MM-DD format.")
    
    threading.Thread(target=run_sequence).start()

def main_gui():
    root = tk.Tk()
    root.title("🕰️ Time Machine Simulator")
    root.geometry("500x300")
    root.config(bg="black")

    tk.Label(root, text="Enter a Date (YYYY-MM-DD):", font=("Arial", 14), bg="black", fg="white").pack(pady=10)
    date_entry = tk.Entry(root, font=("Arial", 14), justify="center")
    date_entry.pack(pady=5)

    output_label = tk.Label(root, text="", font=("Arial", 13), bg="black", fg="cyan", wraplength=450)
    output_label.pack(pady=30)

    go_button = tk.Button(root, text="🚀 Begin Time Travel", font=("Arial", 14), bg="darkblue", fg="white",
                          command=lambda: simulate_time_travel(date_entry, output_label))
    go_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main_gui()
