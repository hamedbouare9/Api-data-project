"""
Module containing the DatabaseHandler class for database setup and data loading
"""

import logging
import os
import json
import pymongo
from utils.constants import DATABASE_CONFIG


class DatabaseHandler:
    """
    Class for handling database setup and data loading
    """

    def __init__(self, paths: list[str], collection_names: list[str], database: dict[str, str] = DATABASE_CONFIG):
        """
        Initialize DatabaseHandler instance.

        Args:
            paths (list[str]): List containing paths to JSON files.
            collection_names (list[str]): List containing the collection names.
            database (dict[str, str]): Dictionary containing the database parameters.
        """
        if len(paths) < 2:
            raise ValueError("Please check your paths, we need two elements")

        self.file_paths = paths
        self.collection_names = collection_names
        self.db_name = database['name']
        self.client = pymongo.MongoClient(database['url'])
        self.db_connect = self.client[self.db_name]
        self.db_list = self.client.list_databases()

    def check_all_paths(self) -> bool:
        """
        Checks if paths exist.

        Returns:
            bool: True if all paths exist, False otherwise.
        """
        return all(os.path.exists(path) for path in self.file_paths)

    def load_data(self):
        """
        Loads the JSON files and inserts them into the database.
        """
        if self.check_all_paths():
            try:
                for i, file_path in enumerate(self.file_paths):
                    with open(file_path, 'r') as file:
                        file_data = json.load(file)
                        if isinstance(file_data, list):
                            self.db_connect[self.collection_names[i]].insert_many(file_data)
                        else:
                            self.db_connect[self.collection_names[i]].insert_one(file_data)
            except KeyError as e:
                logging.info(e)
            finally:
                self.client.close()
        else:
            raise Exception('Please provide the correct filepath')

    def find_database_name(self) -> bool:
        """
        Check if db_name exists on MongoDB list.

        Returns:
            bool: True if the database name exists, False otherwise.
        """
        return any(self.db_name in db.values() for db in self.db_list)

    def create_database(self):
        """
        Create database if it does not exist.
        """
        if not self.find_database_name():
            self.load_data()
            logging.info('The database has been created')
        else:
            logging.info('The database already exists')