import os
os.system("pip install selenium==3.141.0")
from webbot import Browser
import time

driver = Browser()

driver.go_to(url='https://google.com')

driver.new_tab(url='https://google.com/account/about')

driver.new_tab(url='https://www.coolmathgames.com')

driver.new_tab(url='https://www.youtube.com')


input("Service is running")