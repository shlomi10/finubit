BASE_URL = "https://taskmaster.com/tasks/"
TASK_ID = "123"
OTHER_TASK_ID = "10"
AUTHORIZATION = "123456789"

EXPECTED_STATUS_CODE = 200
EXPECTED_CONTENT_TYPE = "application/json"
EXPECTED_TITLE = 'Complete API Testing Practice'
EXPECTED_DESCRIPTION = 'Test cases and execute them for API testing practice'
EXPECTED_DUE_DATE = '2024-05-01'

EXPECTED_NEW_POST_TITLE = 'Complete API Testing Practice'
EXPECTED_NEW_POST_DESCRIPTION = 'Write test cases and execute them for API testing practice'
EXPECTED_NEW_POST_DUE_DATE = '2024-07-01'

EXPECTED_PUT_TITLE = 'update put'
EXPECTED_PUT_DESCRIPTION = 'update test case for put test'
EXPECTED_PUT_DUE_DATE = '2024-08-01'

NEW_TASK = {
    "title": 'Complete API Testing Practice',
    "description": 'Write test cases and execute them for API testing practice',
    "due_date": '2024-07-01'
}

UPDATE_TASK_PUT = {
    "title": 'update put',
    "description": 'update test case for put test',
    "due_date": '2024-08-01'
}
