from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common.base_page import BasePage
from locators.wikipedia_locators import WikiPediaLocators

class WikiPage(BasePage):
    def open(self):
        self.driver.get(self.config['urls']['wikipedia'])

    def validate_wikipedia_logo(self):
        wikipedia_logo = self.find_element(WikiPediaLocators.wikipedia_logo)
        assert wikipedia_logo.is_displayed(), "Wikipedia logo is not displayed"

    def search_input_value(self, search_text):
        search_box = self.find_clickable_element(WikiPediaLocators.search_box)
        search_box.clear()
        search_box.send_keys(search_text + Keys.ENTER)
    
    def click_partial_link(self):
        partial_link_text = self.find_clickable_element(WikiPediaLocators.partial_link)
        partial_link_text.click()
    
    def validate_header_text(self):
        header_text = self.find_element(WikiPediaLocators.header_text)
        assert header_text.is_displayed(), "2022–23 IR Tanger season is not displayed"