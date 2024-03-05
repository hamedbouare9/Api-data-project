"""
Configuration file for database setup in the project
"""

# Define collection names
COLLECTION_NAMES = ['sealk-profiles', 'sealk-interactions']

# Define file paths for data storage
FILE_PATHS = ['./data/sealk-profiles.json', './data/sealk-interactions.json']

# Database configuration
DATABASE_CONFIG = {
    'name': 'mydatabase',
    'url': 'mongodb://localhost:27017/'
}