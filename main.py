from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from time import sleep
from colored import fg, attr
from helpers import wait_for_page_load, color
from config import NETWORK_SSID, 5G_PRESENT

gateway_url = 'http://192.168.0.1'

chrome_options = Options()
chrome_options.add_argument('--headless=new')
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) # disable logs from printing
# chrome_options.add_experimental_option("detach", True) # keeps browser open until manual (mouse) close
print(color('Starting webdriver... ', 'green') + color('[1/5]', 'red'))
driver = webdriver.Chrome(options=chrome_options)

print(color('Waiting for gateway sign-in page to load... ', 'green') + color('[2/5]', 'red'))
driver.get(gateway_url)
wait_for_page_load(driver, 'tr_UserName')
wait_for_page_load(driver, 'tr_Password')

username_input = driver.find_element(By.ID, "UserName")
username_input.send_keys('admin')

password_input = driver.find_element(By.ID, "Password")
password_input.send_keys('password')

submit_button = driver.find_element(By.CLASS_NAME, "submitBtn")
submit_button.click()
print(color('Waiting for default portal to load... ', 'green') + color('[3/5]', 'red'))
wait_for_page_load(driver, 'BasicSetup')

driver.get(gateway_url + '?util_status')
print(color('Waiting for page with information to load... ', 'green') + color('[4/5]', 'red'))
wait_for_page_load(driver, 'NoofWifiClients')

print(color('Parsing information... ', 'green') + color('[5/5]', 'red'))
soup = BeautifulSoup(driver.page_source, 'html.parser')

if 5G_PRESENT:
    no_2_4GHz, no_5GHz = [el.get_attribute_list('value')[0] for el in [soup.find(id='NoofWifiClients'), soup.find(id='NoofWifiClients50')]]
    print()
    print(f"   {color(f'{NETWORK_SSID}:', 'green')} {color(no_2_4GHz, 'red')} Wi-Fi Clients")
    print(f"{color(f'{NETWORK_SSID}-5G:', 'green')} {color(no_5GHz, 'red')} Wi-Fi Clients")
else:
    no_2_4GHz = soup.find(id='NoofWifiClients').get_attribute_list('value')[0]
    print()
    print(f"   {color(f'{NETWORK_SSID}:', 'green')} {color(no_2_4GHz, 'red')} Wi-Fi Clients")
