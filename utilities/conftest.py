import pytest

from utilities.constants import *
from utilities.requestsUtilities import RequestsUtility
from utilities.validations import Validations


@pytest.fixture()
def setup():
    requests_utility = RequestsUtility()
    validations = Validations()
    response = requests_utility.get_response(BASE_URL, TASK_ID)
    yield requests_utility, validations, response


@pytest.fixture()
def setup_post():
    requests_utility = RequestsUtility()
    validations = Validations()
    post_new_task = requests_utility.post_call(BASE_URL, NEW_TASK)
    yield requests_utility, validations, post_new_task


@pytest.fixture()
def setup_put():
    requests_utility = RequestsUtility()
    validations = Validations()
    put_task = requests_utility.put_call(BASE_URL + TASK_ID, UPDATE_TASK_PUT)
    yield requests_utility, validations, put_task
