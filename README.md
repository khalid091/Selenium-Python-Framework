# Selenium Python Automation Framework

A robust test automation framework built with Python, Selenium, and Behave for BDD testing.

## Project Structure

```
├── config/
│   └── config.yaml           # Configuration settings
├── drivers/
│   └── chromedriver.exe      # Chrome WebDriver
├── features/
│   ├── environment.py        # Behave hooks and setup
│   ├── steps/
│   │   └── wikipedia_steps.py # Step definitions
│   └── wikipedia.feature     # BDD feature files
├── locators/
│   └── wikipedia_locators.py # Page element locators
├── pages/
│   ├── base_page.py         # Base page object with common methods
│   └── wiki_page.py         # Wikipedia page object
├── requirements.txt         # Project dependencies
└── README.md               # Project documentation
```

## Setup Instructions

1. **Prerequisites**
   - Python 3.8 or higher
   - Chrome browser installed
   - pip (Python package manager)

2. **Installation**
   ```bash
   # Clone the repository
   git clone <repository-url>
   cd <project-directory>

   # Create and activate virtual environment (optional but recommended)
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt
   ```

3. **ChromeDriver Setup**
   - Ensure ChromeDriver version matches your Chrome browser version
   - Place ChromeDriver in the `drivers` directory
   - Update the path in `environment.py` if needed

## Running Tests

```bash
# Run all tests
behave

# Run specific feature
behave features/wikipedia.feature

# Run with specific tags
behave --tags @smoke

# Run with detailed logging
behave -v
```

## Key Features

- **Page Object Model**: Organized page interactions and element locators
- **BDD Testing**: Behavior-driven development with Behave
- **Robust Error Handling**: Custom exceptions and logging
- **Configurable**: YAML-based configuration
- **Cross-browser Support**: Ready for multiple browser implementations

## Maintenance Notes

### 1. Element Locators
- Keep locators in separate files for easy maintenance
- Use meaningful names for locator variables
- Consider using CSS selectors over XPath when possible
- Regularly verify locators as websites change

### 2. Error Handling
- Check `base_page.py` for custom exception handling
- Review logging levels in `base_page.py`
- Monitor for new types of exceptions that might need handling

### 3. Performance
- Review wait times in `base_page.py`
- Consider implementing parallel test execution
- Monitor test execution time

### 4. Browser Compatibility
- Test with different Chrome versions
- Consider adding support for other browsers
- Keep ChromeDriver updated

## Common Issues and Solutions

1. **StaleElementReferenceException**
   - Implement proper wait conditions
   - Use `wait_for_page_load()` before element interaction
   - Consider using `@retry` decorator for flaky elements

2. **ElementNotVisibleError**
   - Check if element is in viewport
   - Verify element's CSS properties
   - Ensure proper page load before interaction

3. **TimeoutException**
   - Review wait times in `base_page.py`
   - Check network connectivity
   - Verify element locators

## Best Practices

1. **Test Organization**
   - Keep feature files focused and atomic
   - Use meaningful scenario names
   - Follow BDD best practices

2. **Code Quality**
   - Follow PEP 8 guidelines
   - Write clear docstrings
   - Use type hints where possible

3. **Maintenance**
   - Regular dependency updates
   - ChromeDriver version checks
   - Test suite review

## Future Improvements

1. **Framework Enhancements**
   - [ ] Add support for parallel test execution
   - [ ] Implement screenshot capture on failure
   - [ ] Add HTML test reports
   - [ ] Integrate with CI/CD pipeline

2. **Test Coverage**
   - [ ] Add more test scenarios
   - [ ] Implement API testing
   - [ ] Add mobile testing support

3. **Documentation**
   - [ ] Add API documentation
   - [ ] Create contribution guidelines
   - [ ] Add more code examples

#Other Information

1. **Creating virtual environment**

   A virtual environment is a self-contained directory that contains all the necessary Python libraries and dependencies for your project. This allows you to isolate your project’s dependencies and avoid any conflicts with your global Python setup.
   
       - Navigate to your project root directory using the terminal or command prompt.
       - Run the following command to create a virtual environment named venv: python -m venv venv
       - Activate the Virtual Environment: venv\Scripts\activate
       - After activation, you'll notice (venv) in the terminal prompt, indicating that the virtual environment is active.


2. **Changing the logger from warning to debugger**

   By changing the logging level to DEBUG, you will receive detailed information from the Selenium WebDriver (selenium.webdriver.remote.remote_connection) and the urllib3 connection pool, which can help you understand what happened before an error occurred.
   
   If you want to change it from warning to debug, follow the steps below:
   
       - Open the base_page.py file in your project.
       - Locate the following logging configuration:
   
               logging.basicConfig(
               level=logging.WARNING,  # Only show WARNING and above
               format='%(levelname)s: %(message)s',  # Simpler format
               datefmt='%H:%M:%S'
           )
           
       - Modify the level=logging.WARNING to level=logging.DEBUG to enable debugging logs. It should look like this:
   
               logging.basicConfig(
               level=logging.DEBUG,  # Show DEBUG level logs and above
               format='%(levelname)s: %(message)s',
               datefmt='%H:%M:%S'
           )

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request


## Contact

For questions or support, please open an issue in the repository. 
