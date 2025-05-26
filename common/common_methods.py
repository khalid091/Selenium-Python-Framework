from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException, ElementNotVisibleException
import yaml
from utils.logger import logger
from utils.exceptions import ElementNotFoundError, ElementNotClickableError, ElementVisibilityTimeoutError

class BasePage:
    """Base class for all page objects"""
    def __init__(self, driver, config):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.config = config
        self.element_finder = ElementFinder(driver, self.wait)
        self.element_waiter = ElementWaiter(driver, self.wait)

class ElementFinder:
    """Class for finding elements with different conditions"""
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def find_element(self, locator):
        """Find element with explicit wait"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            if not element.is_displayed():
                logger.warning(f"Element found but not visible: {locator}")
                raise ElementNotVisibleException(f"Element found but not visible with locator: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Element not found: {locator}")
            raise ElementNotFoundError(f"Element not found with locator: {locator}")
        except StaleElementReferenceException:
            logger.error(f"Element became stale: {locator}")
            raise ElementNotFoundError(f"Element became stale with locator: {locator}")

    def find_clickable_element(self, locator):
        """Find clickable element with explicit wait"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            if not element.is_displayed():
                logger.warning(f"Element found but not visible: {locator}")
                raise ElementNotVisibleException(f"Element found but not visible with locator: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Element not clickable: {locator}")
            raise ElementNotClickableError(f"Element not clickable with locator: {locator}")
        except ElementClickInterceptedException:
            logger.error(f"Element click intercepted: {locator}")
            raise ElementNotClickableError(f"Element click intercepted with locator: {locator}")
        except StaleElementReferenceException:
            logger.error(f"Element became stale: {locator}")
            raise ElementNotClickableError(f"Element became stale with locator: {locator}")

    def find_visible_element(self, locator):
        """Find visible element with explicit wait"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            if not element.is_displayed():
                logger.warning(f"Element found but not visible: {locator}")
                raise ElementNotVisibleException(f"Element found but not visible with locator: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Element not visible: {locator}")
            raise ElementNotVisibleException(f"Element not visible with locator: {locator}")
        except StaleElementReferenceException:
            logger.error(f"Element became stale: {locator}")
            raise ElementNotVisibleException(f"Element became stale with locator: {locator}")

class ElementWaiter:
    """Class for waiting on elements with different conditions"""
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def wait_for_element_to_disappear(self, locator):
        """Wait for element to disappear"""
        try:
            return self.wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            logger.error(f"Element did not disappear: {locator}")
            raise ElementNotVisibleException(f"Element did not disappear with locator: {locator}")
        except StaleElementReferenceException:
            logger.error(f"Element became stale: {locator}")
            raise ElementNotVisibleException(f"Element became stale with locator: {locator}")

    def wait_for_page_load(self):
        """Wait for the page to be fully loaded"""
        try:
            self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        except TimeoutException:
            logger.error("Page did not load completely")
            raise TimeoutException("Page did not load completely") 