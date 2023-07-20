import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import threading
import time

def set_alarm():
    alarm_time_str = alarm_time_entry.get()
    try:
        alarm_time = datetime.strptime(alarm_time_str, "%H:%M:%S")
    except ValueError:
        messagebox.showerror("Invalid Time Format", "Please use HH:MM:SS format for the alarm time.")
        return

    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=f"Alarm set for {alarm_time.strftime('%H:%M:%S')}")

    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time_str:
            messagebox.showinfo("Alarm", "Wake up! It's time!")
            break
        time.sleep(1)

def start_alarm_thread():
    thread = threading.Thread(target=set_alarm)
    thread.daemon = True
    thread.start()

root = tk.Tk()
root.title("Alarm Clock")

time_label = tk.Label(root, text="00:00:00", font=("Arial", 40))
time_label.pack()

alarm_time_entry = tk.Entry(root, font=("Arial", 20))
alarm_time_entry.pack()

set_alarm_button = tk.Button(root, text="Set Alarm", font=("Arial", 14), command=start_alarm_thread)
set_alarm_button.pack(pady=10)

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)

update_time()  # Start updating the time every second

root.mainloop()
