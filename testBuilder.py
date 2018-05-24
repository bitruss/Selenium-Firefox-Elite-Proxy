"""
	I got this tutorial from youtube\
	Title: Python Selenium Set HTTP Proxy Firefox Profile
	Link : https://www.youtube.com/watch?v=eIc8YdwB0LI
	
	By @DevNami on Youtube
"""

from selenium import webdriver
import time
import proxyBuilder as pb


HOST = pb._getIP()#"58.74.78.19"
PORT = pb._getPort()#80
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxyhttp", HOST)
profile.set_preference("network.proxy.http_port", PORT)
profile.set_preference("network.proxy.ssl", HOST)
profile.set_preference("network.proxy.ssl_port", PORT)
profile.update_preferences()

driver= webdriver.Firefox(firefox_profile=profile)
driver.get("https://www.whatismyip.com/")
time.sleep(3)
driver.close()
