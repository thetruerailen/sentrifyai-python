import requests
from .config import BASE_URL
from .exceptions import ModelNotFoundError, APIRequestError

class SentrifyAI:
    def __init__(self):
        pass

    def list_models(self):
        try:
            response = requests.get(f'{BASE_URL}models')
            response.raise_for_status()
            return response.json()['models']
        except requests.exceptions.HTTPError as e:
            raise APIRequestError(f'HTTP error occurred: {e}')
        except requests.exceptions.RequestException as e:
            raise APIRequestError(f'Request exception occurred: {e}')

    def classify_message(self, model_slug, message):
        try:
            params = {
                'model': model_slug,
                'message': message
            }
            response = requests.get(f'{BASE_URL}moderation', params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                raise ModelNotFoundError(f'Model {model_slug} not found.')
            raise APIRequestError(f'HTTP error occurred: {e}')
        except requests.exceptions.RequestException as e:
            raise APIRequestError(f'Request exception occurred: {e}')
