from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def before_scenario(context, scenario):
    """Before each scenario, initialize the WebDriver and clear browser cache."""
    options = Options()
    service = Service(executable_path="F:\\Automation\\SeleniumPython\\drivers\\chromedriver.exe")
    context.driver = webdriver.Chrome(service=service, options=options)
    # context.driver.maximize_window()
    
    # Clear browser cache and cookies
    context.driver.execute_cdp_cmd('Network.clearBrowserCache', {})
    context.driver.execute_cdp_cmd('Network.clearBrowserCookies', {})
    context.driver.delete_all_cookies()

def after_scenario(context, scenario):
    """After each scenario, quit the WebDriver."""
    if hasattr(context, 'driver'):
        time.sleep(5)
        context.driver.quit()
