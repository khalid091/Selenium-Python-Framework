from behave import given, when, then
from pages.wiki_page import WikiPage

@given('User navigate to Wikipedia')
def navigate_to_wikipedia(context):
    # The browser is already opened in environment.py
    context.wiki_page = WikiPage(context.driver)
    context.wiki_page.open()

@when('User validate the wikipedia logo')
def validate_wikipedia_logo(context):
    context.wiki_page.validate_wikipedia_logo()

@when('User search for "{search_text}"')
def search_for_ir_tanger(context, search_text):
    context.wiki_page.search_input_value(search_text)

@when('User click the link')
def click_the_ir_tanger_link(context):
    context.wiki_page.click_partial_link()

@then('User validate the header text')
def validate_ir_tanger_text(context):
    context.wiki_page.validate_header_text()