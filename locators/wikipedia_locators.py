from selenium.webdriver.common.by import By

class WikiPediaLocators:
    # Store locators as class variables for reusability
    wikipedia_logo = (By.CLASS_NAME, "central-featured")
    search_box = (By.ID, "searchInput")
    partial_link = (By.PARTIAL_LINK_TEXT, "2022–23 IR Tanger season")
    header_text = (By.XPATH, "//span[text()='2022–23 IR Tanger season']")
