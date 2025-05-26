from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException, ElementNotVisibleException
import yaml
import logging

# Configure logging with a cleaner format and higher level
logging.basicConfig(
    level=logging.WARNING,  # Only show WARNING and above
    format='%(levelname)s: %(message)s',  # Simpler format
    datefmt='%H:%M:%S'
)

# Disable selenium and urllib3 debug logs
logging.getLogger('selenium').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

class ElementNotFoundError(Exception):
    """Raised when an element cannot be found"""
    pass

class ElementNotClickableError(Exception):
    """Raised when an element is not clickable"""
    pass

class ElementNotVisibleError(Exception):
    """Raised when an element is not visible"""
    pass

class ElementVisibilityTimeoutError(Exception):
    """Raised when an element is found but not visible within the timeout period"""
    pass

class BasePage:
    def __init__(self, driver, config):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.config = config

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
