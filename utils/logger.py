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

# Create and export logger instance
logger = logging.getLogger(__name__) 