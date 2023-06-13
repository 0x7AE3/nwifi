from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from time import sleep
from colored import fg, attr

def wait_for_page_load(driver, element_id, delay=100):
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, element_id)))
    except TimeoutException:
        print('Page taking too long to load, stopping execution...')
        exit()

# colors a string
def color(text, color):
    return f'{fg(color)}{text}{attr("reset")}'
