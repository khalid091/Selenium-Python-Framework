class ElementNotFoundError(Exception):
    """Raised when an element cannot be found"""
    pass

class ElementNotClickableError(Exception):
    """Raised when an element is not clickable"""
    pass

class ElementVisibilityTimeoutError(Exception):
    """Raised when an element is found but not visible within the timeout period"""
    pass 