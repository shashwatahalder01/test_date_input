import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

# from telnetlib import EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
            def __init__(self, driver, base_url="about:blank"):
                self.base_url = base_url
                self.driver = driver
                self.timeout = 30

            def find_element(self, *locator):
                return self.driver.find_element(*locator)

            def find_elements(self, *locator):
                return self.driver.find_elements(*locator)

            def open(self, url):
                url = self.base_url + url
                self.driver.get(url)

            def get_title(self):
                return self.driver.title

            def get_url(self):
                return self.driver.current_url

            def refresh(self):
                return self.driver.refresh()

            def hover(self, *locator):
                element = self.find_element(*locator)
                hover = ActionChains(self.driver).move_to_element(element)
                hover.perform()

            def wait_element(self, *locator):
                try:
                    WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
                except TimeoutException:
                    print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
                    self.driver.quit()
