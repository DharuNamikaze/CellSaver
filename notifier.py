from plyer import notification
# This is for the Annoying Popp-up Windows Notification.
def notify_user(wear_level):
    if wear_level > 10 and wear_level<=20:
        notification.notify(
            title="Battery Health Notification",
            message=f"Your battery's wear level is {wear_level:.2f}%. \nThis is still good, The battery has some wear but is generally performing well.",
            timeout=10
        )
    elif wear_level > 20 and wear_level<=30: 
        notification.notify(
            title="Battery Health Alert",
            message=f"Your battery's wear level is {wear_level:.2f}%. \nThis is a moderate wear level. the is significantly battery is heating up.",
            timeout=10
        )
    elif wear_level > 30 and wear_level<=40: 
        notification.notify(
            title="Battery Health Alert",
            message=f"Your battery's wear level is {wear_level:.2f}%. \nThis is a serious wear level. The battery may start to show signs of reduced performance, such as shorter battery life.",
            timeout=10
        )  
    else:
        notification.notify(
            title="Battery Health Alert",
            message=f"Your battery's wear level is {wear_level:.2f}%. \nThe battery is heavily Used. It may not hold charge for very long, Consider replacing it soon.",
            timeout=10
        )         
