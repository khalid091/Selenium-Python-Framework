Feature: Wikipedia Search

  Scenario: Search for "Khalid Bahaj" and validate globe icon
    Given User navigate to Wikipedia
    When User validate the wikipedia logo
    When User search for "Khalid Bahaj"
    When User click the link
    Then User validate the header text