"""
Script to create instances of DatabaseHandler class and set up the database
"""

from database_handler import DatabaseHandler
from utils.constants import DB, COLLECTION_NAMES, FILE_PATHS
import logging

def main():
    """
    Main function to create DatabaseHandler instance and set up the database
    """
    try:
        new_instance = DatabaseHandler(FILE_PATHS, COLLECTION_NAMES, DB)
        new_instance.create_database()
        logging.info('Database setup completed successfully.')
    except Exception as e:
        logging.error(f'Error occurred during database setup: {str(e)}')

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    # Run main function
    main()
