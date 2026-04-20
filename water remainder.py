import time
# install plyer module from pip for desktop notification
from plyer import notification
#Star the rema#Water remainder project

print("Water Reminder Started")

# Stop remainder 

print("Press  Ctrl + c to stop")

try:
    while True:
        notification.notify(
            title="💧 Water Reminder",
            message="Abdullah drink water now! Stay hydrated",
            timeout=30
        )
        time.sleep(100)

except KeyboardInterrupt:
    print("\nWater Reminder Stopped")
