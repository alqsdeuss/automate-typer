import pyautogui
import webbrowser
import time

webbrowser.open("https://discord.com/api/v9/channels/ID")

time.sleep(5)

message = "suck"

for i in range(100):
    pyautogui.write(message)
    pyautogui.press("enter")
