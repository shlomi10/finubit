import requests
import json

from requests.cookies import RequestsCookieJar
from requests.structures import CaseInsensitiveDict

from utilities.constants import AUTHORIZATION


class RequestsUtility:

    # GET status code
    def get_status_code(self, resp) -> int:
        return resp.status_code

    # Get headers
    def get_headers(self, resp) -> CaseInsensitiveDict[str]:
        return resp.headers

    def get_cookies(self, resp) -> RequestsCookieJar:
        return resp.cookies

    # Get content type
    def get_content_type(self, resp) -> str:
        return resp.headers['Content-Type']

    # Create GET request + Base URL as JSON
    def get_response_as_json(self, resp) -> json:
        return resp.json()

    # Create GET request + Base URL
    def get_response(self, base_url: str = "", prefix: str = "", params: str = "") -> requests:
        return requests.get(base_url + prefix, params=params, auth=AUTHORIZATION)

    # Create POST request
    def post_call(self, base_url: str = "", obj: str = "", cookies: str = "") -> requests:
        return requests.post(base_url, json=obj, cookies=cookies, auth=AUTHORIZATION)

    # Create PUT call
    def put_call(self, base_url: str = "", prefix: str = "", update_obj: str = "") -> json:
        return requests.put(base_url + prefix, json=update_obj, auth=AUTHORIZATION)
