import json
import requests as re


def verify_status_code(func) -> dict | list:
    def inner(*args, **kwargs):
        response: re.Response = func(*args, **kwargs)
        if response.status_code not in [200, 201]:
            raise ConnectionRefusedError(response.status_code,
                                         response.text)
        return response.json()
    return inner


class Request:
    @verify_status_code
    def get(url: str,
            headers: dict = None,
            params: dict = None) -> re.Response:
        """
        Sends a GET request to the specified URL with optional headers and parameters and parses the response as a JSON object.

        Args:
            url (str): The URL to send the GET request to.
            headers (dict, optional): The headers to include in the request. Defaults to None.
            params (dict, optional): The parameters to include in the request. Defaults to None.

        Returns:
            json.loads: The response from the GET request, parsed as a JSON object.
        """

        if not headers:
            headers = {}

        # Required for LinkedIn
        headers['X-Restli-Protocol-Version'] = '2.0.0'

        return re.get(url, headers=headers, params=params)

    @verify_status_code
    def post(url: str,
             headers: dict = None,
             params: dict = None,
             data: dict | str = None) -> re.Response:
        """
        Sends a POST request to the specified URL with optional headers, parameters, and data.

        Args:
            url (str): The URL to send the POST request to.
            headers (dict, optional): The headers to include in the request. Defaults to None.
            params (dict, optional): The parameters to include in the request. Defaults to None.
            data (dict, optional): The data to include in the request. Defaults to None.

        Returns:
            json.loads: The response from the POST request, parsed as a JSON object.
        """

        if not headers:
            headers = {}

        # Required for LinkedIn
        headers['X-Restli-Protocol-Version'] = '2.0.0'

        if isinstance(data, dict):
            data = json.dumps(data)

        return re.post(url, headers=headers, params=params, data=data)
