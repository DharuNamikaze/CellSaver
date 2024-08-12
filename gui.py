import tkinter as tk
from battery_monitor import extract_battery_health, generate_battery_report
from notifier import notify_user

def check_battery():
    data = generate_battery_report()
    wear_level = extract_battery_health(data)
    if wear_level >10 and wear_level<=20:
        battery_status_label.config(text=f"Current Battery Wear Level: {wear_level:.2f}% \n The battery is in great shape, with minimal wear.")
        notify_user(wear_level)
    elif wear_level >20 and wear_level<=30:
        battery_status_label.config(text=f"Current Battery Wear Level: {wear_level:.2f}% \n Tip: Keep an eye on it. If it reaches 30% or more, you may start experiencing issues.")
        notify_user(wear_level)
    elif wear_level >30 and wear_level<=40:
        battery_status_label.config(text=f"Current Battery Wear Level: {wear_level:.2f}% \n Tip: Consider planning for a battery replacement.")
        notify_user(wear_level)
    elif wear_level >40:
        battery_status_label.config(text=f"Current Battery Wear Level: {wear_level:.2f}% \n Tip: It's advisable to replace the battery to ensure your device runs smoothly..")
        notify_user(wear_level)
    else:
        battery_status_label.config(text="The battery health is Excellent.")

app = tk.Tk()
app.title("Battery Health Notifier")
app.minsize(width=450, height=300)
app.configure(bg="#282C34")

# Creating label
battery_status_label = tk.Label(app, text="Check your battery Health status \n\n Regular monitoring helps you stay aware of any changes, \n make decisions about when to replace the battery.", font=("Poppins", 12), bg="#282C34", fg="white")
battery_status_label.pack(pady=40)

# Creating a frame to hold the button
button_frame = tk.Frame(app, bg="#282C34")
button_frame.pack(side="bottom", fill="x", pady=10)

# set the button inside the frame
check_button = tk.Button(button_frame, text="Check Now", command=check_battery, font=("Poppins", 12))
check_button.pack(pady=10)

app.mainloop()

# Created by ig: @dharu_namikaze