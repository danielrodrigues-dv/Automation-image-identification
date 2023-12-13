import webbrowser
from time import sleep
import pyautogui

url = "https://www.google.com/recaptcha/api2/demo"
webbrowser.open(url)
sleep(4)
captcha = pyautogui.locateCenterOnScreen('img.png')
pyautogui.click(captcha[0], captcha[1], duration=2)
