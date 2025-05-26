# Selenium Python BDD Framework

This project is a Behavior-Driven Development (BDD) framework using Selenium WebDriver with Python, implementing the Page Object Model design pattern.

## Project Structure

```
project_root/
├── common/                      # Common functionality and base classes
│   └── common_methods.py        # Contains BasePage, ElementFinder, and ElementWaiter classes
├── pages/                       # Page Object classes
│   └── wiki_page.py            # Wikipedia page object
├── features/                    # BDD feature files and step definitions
│   ├── environment.py          # Behave environment setup
│   ├── wikipedia.feature       # Feature file for Wikipedia tests
│   └── steps/                  # Step definition files
│       └── wikipedia_steps.py  # Step definitions for Wikipedia tests
├── utils/                      # Utility modules
│   ├── exceptions.py           # Custom exception classes
│   └── logger.py              # Logging configuration
├── locators/                   # Element locators
│   └── wikipedia_locators.py   # Locators for Wikipedia page
├── config/                     # Configuration files
│   └── config.yaml            # Configuration settings
├── drivers/                    # WebDriver executables
│   └── chromedriver.exe       # Chrome WebDriver
├── requirements.txt            # Project dependencies
└── README.md                  # Project documentation
```

## Key Components

### Common Methods (`common/common_methods.py`)
- `BasePage`: Base class for all page objects
- `ElementFinder`: Handles element finding operations
- `ElementWaiter`: Handles element waiting operations

### Page Objects (`pages/`)
- Contains page-specific classes that inherit from `BasePage`
- Each page object represents a web page and its functionality

### Features (`features/`)
- Contains BDD feature files written in Gherkin syntax
- Step definitions that implement the feature scenarios

### Utils (`utils/`)
- `exceptions.py`: Custom exception classes for better error handling
- `logger.py`: Centralized logging configuration

### Locators (`locators/`)
- Contains element locators organized by page
- Uses a class-based approach for better organization

### Configuration (`config/`)
- `config.yaml`: Contains configuration settings like URLs and driver paths

## Setup and Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the appropriate WebDriver for your browser and place it in the `drivers/` directory.

## Running Tests

To run the tests:
```bash
behave
```

To run with specific tags:
```bash
behave --tags=@tag_name
```

## Best Practices

1. **Page Object Model**: Each web page has its own class that inherits from `BasePage`
2. **Element Locators**: All locators are stored in separate files for better maintenance
3. **Configuration Management**: Uses YAML for configuration settings
4. **Error Handling**: Custom exceptions for better error management
5. **Logging**: Centralized logging configuration for better debugging
6. **Code Organization**: Clear separation of concerns with distinct classes for different functionalities

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

   A virtual environment is a self-contained directory that contains all the necessary Python libraries and dependencies for your project. This allows you to isolate your project's dependencies and avoid any conflicts with your global Python setup.
   
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
