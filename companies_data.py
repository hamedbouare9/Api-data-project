"""
Module containing the CompaniesData class for project usage
"""

import logging
from utils.constants import DATABASE_CONFIG, COLLECTION_NAMES, FILE_PATHS
from database_handler import DatabaseHandler


class CompaniesData(DatabaseHandler):
    """
    Class for handling company data in the project
    """

    def __init__(self, id_item: str, paths: list[str] = FILE_PATHS,
                 collections_names: list[str] = COLLECTION_NAMES, database: dict[str, str] = DATABASE_CONFIG):
        """
        Initialize CompaniesData instance.
        """
        super().__init__(paths, collections_names, database)
        self.id = id_item
        try:
            self.data_filtered = list(self.db_connect[self.collection_names[1]].find({"subject.id": self.id}))
        except KeyError as e:
            logging.info(e)

    def count_number_interactions(self) -> int:
        """
        Count the number of interactions for the current profile.

        Returns:
            int: Number of interactions
        """
        return len(self.data_filtered)

    def get_targeted_companies_names(self) -> list[str]:
        """
        Get the names of targeted companies.

        Returns:
            list[str]: Names of targeted companies
        """
        all_companies_name = []
        for obj in self.data_filtered:
            company_id = obj['object']['id']
            result_filtered = self.db_connect[self.collection_names[0]].find({"source.id": company_id})
            company_name = list(result_filtered)[0]['name']
            all_companies_name.append(company_name)
        return all_companies_name