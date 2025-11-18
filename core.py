from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Core:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.get_element(locator).click()

    def get_element(self, locator, timeout=60):
      try:
          return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
      except Exception as e:
          pytest.fail('{}'.format(e))

    def wait_until_element_visible(self, locator, timeout=60):
      try:
          return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
      except:
          return False
