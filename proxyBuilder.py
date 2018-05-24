from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from random import randint

# Run Firefox as headless because we don't want a browser window to pop-up
options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(firefox_options=options)
driver.get("http://www.gatherproxy.com/proxylist/anonymity/?t=Elite")

_randNum = randint(3, 27)

# From the page-source structure,  the 'tr' tag in the 'tbody' have two tr's that we want to ignore
# and the page displays 25 Elite IP addresses and ports
# From above we generated a random number between 3 and 27 to pick an IP randomly while ignoring the 
# first two 'tr' tags
_ip = driver.find_element_by_xpath("//div[@class='proxy-list']/table/tbody/tr[%d]/td[2]"%_randNum).text
_port = driver.find_element_by_xpath("//div[@class='proxy-list']/table/tbody/tr[%d]/td[3]"%_randNum).text

def _getIP():
	global _ip
	return _ip
def _getPort():
	global _port
	return int(_port)
driver.close()
