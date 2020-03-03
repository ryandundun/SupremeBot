from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


import time
import requests
import bs4
import random
import webbrowser
import csv
import threading

#import pdb
#pdb.set_trace()


# ModelNumber = 'jackets'
# SizeList = ['Medium', 'Large']
# ThreadCount = 10;



#Need to Implement
inStock = False
def checkOut():
	print('I just did something')


def checkStock(url):
	html = requests.get(url, headers=RandomHeaders.LoadHeader(), proxies = proxies) 

	#BeautifulSoup Object that gets the html of the webpage
	page = bs4.BeautifulSoup(html.text, "lxml")

	#Getting product name
	prodName = str(page.select('h1'))
	prodName = prodName.split('name">', 1)[1]
	prodName, trash = prodName.split("</")
	print('___________________________\n')
	print ('ITEM REQUESTED: \n' + 'Model: ' + prodName)

	#Getting product style
	prodStyle = str(page.select('.style'))
	prodStyle = prodStyle.split('model">', 1)[1]
	prodStyle, trash = prodStyle.split("</")
	print ('Style: ' + str(prodStyle))	


	if (str(page.select('.sold-out')) != '[<b class="button sold-out">sold out</b>]'):
	# nah = page.select('.sold-out')
	# if (nah == '.sold-out'):
	# 	return None
		ListOfSizesRaw = page.select('#size')
		Sizes = str(ListOfSizesRaw[0].getText())
		#Sizes = Sizes.replace('\n', ' ')
		#Sizes = Sizes.split()
		print ('\nThese sizes are available:\n' + Sizes)
		inStock = True
		print('___________________________')
		return Sizes
	else:
		print('Sold out')
		print('___________________________')
		return None



def iCarted(product, url):
	try:
		Sizes = checkStock(url)
	except:
		pass

print('----------------------------------------------------\n')
#URL = genURL("jackets","Medium")
prodInfo = raw_input('\n\nPlease enter product alt code: ')
userSize = raw_input('\n\nPlease enter what size you would like: ')
card = 'Mastercard'


# curl = raw_input('\n\nPaste URL Here: ')
curl = 'http://www.supremenewyork.com/shop/all'

print ('\nREDIRECTING TO '+ str(curl) + '\n')

#time.sleep(3)

print('Checking availability...\n')
iCarted('jackets', str(curl))


print('\n\n')
print('----------------------------------------------------')

#webdriver.Firefox/.Chrome
#executable_path="/Users/Richy/Documents/workspace/chromedriver"
driver = webdriver.Chrome(executable_path="/Users/Richy/Documents/PROJECTS/SupremeBot/chromedriver")



driver.get(str(curl))
buyPath = '//input'
contPath='//*[contains(concat( " ", @class, " " ), concat( " ", "continue", " " ))]'
checkOutPath = '//*[contains(concat( " ", @class, " " ), concat( " ", "checkout", " " ))]'

delay = 3
#wait.until(EC.visibility_of_element_located((By.NAME, buyPath)))

#driver.find_element_by_xpath(contPath).click()


try:

		#clicking add to cart
	fullNameXPath = '//*[(@id = "order_billing_name")]'
	emailXPath = '//*[(@id = "order_email")]'
	addrXPath = '//*[@id="bo"]'
	cityXPath = '//*[@id="order_billing_city"]'

	prodInfoXpath = "//img[@alt='" + prodInfo + "']"

	WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, prodInfoXpath)))
	driver.find_element_by_xpath(prodInfoXpath).click()

#Select Size
	WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="s"]')))
	dropdown = Select(driver.find_element_by_xpath('//*[@id="s"]'))
	dropdown.select_by_visible_text(userSize)


#Add to cart
	WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-remove-buttons"]/input')))
	driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()

#Clicking checkout	
	WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cart"]/a[2]')))
	driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()

#Filling in information for checkout
	nameFieldElement = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="order_billing_name"]')))
	nameFieldElement.clear()
	nameFieldElement.send_keys("Richard Feng")


	postXPath = '//*[@id="order_billing_zip"]'
	#New Drop Date code //*[@id="nnb"] USE THIS ONE FOR CARD NUMBER
	cardXPath = '//*[@id="cnb"]'
	#New Drop date codes 
	# //*[@id="orcer"]
	dropCvv = '//*[@id="orcer"]'
	dropCard = '//*[@id="nnb"]'
	dropCheck = '//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins'
	dropProcess = '//*[@id="pay"]/input'
	cvvXPath = '//*[@id="vval"]'
	#//*[@id="cvw"]
	# Checkbox drop date //*[@id="cart-cc"]/fieldset/p[2]/label/div/ins
	# Process drop date //*[@id="pay"]/input



	emailFieldElement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, emailXPath)))
	emailFieldElement.clear()
	emailFieldElement.send_keys("richyfeng@gmail.com")

	phoneFieldElement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="order_tel"]')))
	phoneFieldElement.clear()
	phoneFieldElement.send_keys("2623666718")


	addFieldElement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, addrXPath)))
	addFieldElement.clear()
	addFieldElement.send_keys("19155 Eton Ct.")


	cityFieldElement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, cityXPath)))
	cityFieldElement.clear()
	cityFieldElement.send_keys("Brookfield")


	postFieldElement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, postXPath)))
	postFieldElement.clear()
	postFieldElement.send_keys("53045")

	#time.sleep(2)
#Select State
	#Select(driver.find_element_by_xpath('//*[@id="order_billing_state"]')).select_by_visible_text('WI')

#Select Credit Card Type
	Select(driver.find_element_by_xpath('//*[@id="credit_card_type"]')).select_by_visible_text(card)

	cardFieldElement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[(@id = "nnaerb")]')))
	cardFieldElement.clear()
	cardFieldElement.send_keys('5213331229752655')
	Select(driver.find_element_by_xpath('//*[@id="credit_card_month"]')).select_by_visible_text('02')
	Select(driver.find_element_by_xpath('//*[@id="credit_card_year"]')).select_by_visible_text('2020')

#THIS CVV IS FOR DROP DATE //*[@id="cvw"]

#NON Drop date check //*[@id="cart-cc"]/fieldset/p/label/div/ins

#Drop date finish //*[@id="pay"]/input
	#cvvFieldElement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vval"]')))
	
	#cvvFieldElement.clear()
	#cvvFieldElement.send_keys('263')


	#Drop 06/08 CVV //*[@id="orcer"]
	cvvFieldElement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropCvv)))
	cvvFieldElement.clear()
	cvvFieldElement.send_keys('123')


	time.sleep(2)
	WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, dropCheck))).click()
	WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, dropProcessterm
		))).click()

	#Click box
	#driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div').click()
	# WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="order_terms"]')))
	# WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//*[(@id = "pay")]//input')))


#//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins
#//*[@id="cvw"]
#//*[@id="rmae"]
#//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins
#//*[@id="cart-cc"]/fieldset/p[2]/label/div





except TimeoutException:
		print "Failed Attempt"




