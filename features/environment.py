from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import yaml
import os

def load_project_config():
    """Load configuration from config/config.yaml."""
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        # Adjust the error message to reflect the path used here
        raise FileNotFoundError(f"Config file not found at '{config_path}'")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML config file at '{config_path}': {str(e)}")

def before_all(context):
    """Load configuration before all scenarios."""
    # This is a standard Behave hook to set up context before tests run
    context.config = load_project_config()

def before_scenario(context, scenario):
    """Before each scenario, initialize the WebDriver and clear browser cache."""
    options = Options()
    # Get the driver path from the loaded config
    # Use os.path.join to create a path relative to the project root
    # assuming tests are run from the project root
    chromedriver_path = context.config['webdriver']['chromedriver_executable_path']
    # If the path in config.yaml is relative to the config file itself,
    # you might need to adjust how you join paths here.
    # Assuming it's relative to the project root:
    service = Service(executable_path=chromedriver_path)
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
