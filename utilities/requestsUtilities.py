import requests
import json

from requests.cookies import RequestsCookieJar
from requests.structures import CaseInsensitiveDict

from utilities.constants import AUTHORIZATION


class RequestsUtility:

    # function to get status code
    def get_status_code(self, resp) -> int:
        return resp.status_code

    # function to get content type
    def get_content_type(self, resp) -> str:
        return resp.headers['Content-Type']

    # function to get response as JSON
    def get_response_as_json(self, resp) -> json:
        return resp.json()

    # function to make get request
    def get_response(self, base_url: str = "", prefix: str = "", params: str = "") -> requests:
        return requests.get(base_url + prefix, params=params, auth=AUTHORIZATION)

    # function to make post request
    def post_call(self, base_url: str = "", obj: str = "", cookies: str = "") -> requests:
        return requests.post(base_url, json=obj, cookies=cookies, auth=AUTHORIZATION)

    # function to make put request
    def put_call(self, base_url: str = "", prefix: str = "", update_obj: str = "") -> requests:
        return requests.put(base_url + prefix, json=update_obj, auth=AUTHORIZATION)
