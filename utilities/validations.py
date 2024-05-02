import json

from utilities.constants import *
from utilities.requestsUtilities import RequestsUtility


class Validations(RequestsUtility):

    # validate status code
    def validate_status_code(status_code: int) -> bool:
        if status_code == EXPECTED_STATUS_CODE:
            return True
        return False

    # validate content type
    def validate_content_type(self, content_type: str) -> bool:
        if content_type == EXPECTED_CONTENT_TYPE:
            return True
        return False

    # validate query parameter task id
    def validate_other_call_task_id(self, json_response: json) -> bool:
        if (len(json_response)) > 10:
            return True
        return False

    # validate title
    def validate_title(self, json_response: json, expected_title: str) -> bool:
        if json_response["title"] == expected_title:
            return True
        return False

    # validate description
    def validate_description(self, json_response: json, expected_expected_description: str) -> bool:
        if json_response["description"] == expected_expected_description:
            return True
        return False

    # validate due_date
    def validate_due_date(self, json_response: json, expected_due_date: str) -> bool:
        if json_response["due_date"] == expected_due_date:
            return True
        return False
