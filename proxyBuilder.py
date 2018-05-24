from selenium import webdriver
import time

# We use firefox driver on a link that will give us list of elite proxys
driver = webdriver.Firefox()
driver.get("http://www.gatherproxy.com/proxylist/anonymity/?t=Elite")
SuperClass = driver.find_element_by_class_name('proxy-lists')
