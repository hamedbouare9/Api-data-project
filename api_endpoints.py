"""
Module containing functions to create API endpoints
"""

from fastapi import FastAPI
from pydantic import constr
from companies_data import CompaniesData

app = FastAPI()


@app.get("/profile/{item_id}")
def get_profile_data(item_id: constr(regex="^([A-Z0-9]{,2}){3}-E$")):
    """
    Endpoint to compute the number of interactions and the targeted companies' names for a given profile ID.

    Args:
        item_id (str): The profile ID.

    Returns:
        dict: A dictionary containing the interaction count and targeted companies' names.
    """
    try:
        new_instance = CompaniesData(item_id)
        nb_interactions = new_instance.count_number_interactions()
        companies_names = new_instance.get_targeted_companies_names()
        return {'interaction_count': nb_interactions, 'interaction_targets': companies_names}
    except Exception as e:
        return {'error': str(e)}