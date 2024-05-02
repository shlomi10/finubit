from utilities.conftest import *


@pytest.mark.functional
def test_status_code(setup):
    requests_utility, validations, resp = setup
    assert validations.validate_status_code(requests_utility.get_status_code(resp)), "status code was not 200"


@pytest.mark.functional
def test_content_type(setup):
    requests_utility, validations, resp = setup
    assert validations.validate_content_type(
        requests_utility.get_content_type(resp)), "content type was not application/json"


@pytest.mark.functional
def test_response_query_params(setup):
    requests_utility, validations, resp = setup
    assert validations.validate_other_call_task_id(
        requests_utility.get_response_as_json(
            requests_utility.get_response(BASE_URL, OTHER_TASK_ID))), "other task id was not work"


@pytest.mark.functional
def test_response_title(setup):
    requests_utility, validations, resp = setup
    assert validations.validate_title(
        requests_utility.get_response_as_json(resp), EXPECTED_TITLE), "there is no title in response"


@pytest.mark.functional
def test_response_description(setup):
    requests_utility, validations, resp = setup
    assert validations.validate_description(requests_utility.get_response_as_json(resp),
                                            EXPECTED_DESCRIPTION), "there is no title in response"


@pytest.mark.functional
def test_response_due_date(setup):
    requests_utility, validations, resp = setup
    assert validations.validate_due_date(
        requests_utility.get_response_as_json(resp), EXPECTED_DUE_DATE), "there is no validate_due_date in response"


@pytest.mark.functional
def test_response_status_code_of_create_new_task(setup_post):
    requests_utility, validations, post_new_task = setup_post
    assert validations.validate_status_code(
        requests_utility.get_status_code(post_new_task)), "status code was not 200 in new task"


@pytest.mark.functional
def test_response_content_type_of_create_new_task(setup_post):
    requests_utility, validations, post_new_task = setup_post
    assert validations.validate_content_type(
        requests_utility.get_content_type(post_new_task)), "content type was not in new task application/json"


@pytest.mark.functional
def test_response_title_for_of_create_new_task(setup_post):
    requests_utility, validations, post_new_task = setup_post
    resp = requests_utility.get_content_type(post_new_task)
    assert validations.validate_title(requests_utility.get_response_as_json(resp),
                                      EXPECTED_NEW_POST_TITLE), "title was not in new task response"


@pytest.mark.functional
def test_response_description_of_create_new_task(setup_post):
    requests_utility, validations, post_new_task = setup_post
    resp = requests_utility.get_content_type(post_new_task)
    assert validations.validate_description(
        requests_utility.get_response_as_json(resp),
        EXPECTED_NEW_POST_DESCRIPTION), "description was not in new task response"


@pytest.mark.functional
def test_response_due_date_of_create_new_task(setup_post):
    requests_utility, validations, post_new_task = setup_post
    resp = requests_utility.get_content_type(post_new_task)
    assert validations.validate_due_date(
        requests_utility.get_response_as_json(resp),
        EXPECTED_NEW_POST_DUE_DATE), "due_date was not in new task response"


@pytest.mark.functional
def test_response_status_code_of_put_new_task(setup_put):
    requests_utility, validations, put_task = setup_put()
    resp = requests_utility.get_content_type(put_task)
    assert validations.validate_status_code(
        requests_utility.get_response_as_json(resp)), "status code was not 200"


@pytest.mark.functional
def test_response_content_type_of_put_new_task(setup_put):
    requests_utility, validations, put_task = setup_put()
    resp = requests_utility.get_content_type(put_task)
    assert validations.validate_content_type(
        requests_utility.get_response_as_json(resp)), "content type was not in updated task application/json"


@pytest.mark.functional
def test_response_title_of_put_new_task(setup_put):
    requests_utility, validations, put_task = setup_put()
    resp = requests_utility.get_content_type(put_task)
    assert validations.validate_title(
        requests_utility.get_response_as_json(resp), EXPECTED_PUT_TITLE), "title was not in updated task response"


@pytest.mark.functional
def test_response_description_of_put_new_task(setup_put):
    requests_utility, validations, put_task = setup_put()
    resp = requests_utility.get_content_type(put_task)
    assert validations.validate_description(
        requests_utility.get_response_as_json(resp),
        EXPECTED_PUT_DESCRIPTION), "description was not in updated task response"


@pytest.mark.functional
def test_response_due_date_of_put_new_task(setup_put):
    requests_utility, validations, put_task = setup_put()
    resp = requests_utility.get_content_type(put_task)
    assert validations.validate_due_date(
        requests_utility.get_response_as_json(resp), EXPECTED_PUT_DUE_DATE), "due_date was not in updated task response"
