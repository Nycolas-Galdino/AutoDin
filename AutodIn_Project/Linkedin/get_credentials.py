import os
from datetime import datetime as dt
import dotenv


def get_credentials() -> tuple:
    """
    A function to retrieve credentials from environment variables.
    It loads the dotenv file, checks if the access token has expired, and returns the API key, API secret, access token, and expiration date.
    """
    dotenv.load_dotenv()

    # Check if access token has expired
    if dt.now() > dt.strptime(os.getenv('EXPIRES_IN'), '%d/%m/%Y'):
        raise ValueError('LINKEDIN_ACCESS_TOKEN has expired')

    # Return API key, API secret, access token, and expiration date
    return (os.getenv('LINKEDIN_API_KEY'),
            os.getenv('LINKEDIN_API_SECRET'),
            os.getenv('LINKEDIN_USER_ID'),
            os.getenv('LINKEDIN_ACCESS_TOKEN'),
            os.getenv('EXPIRES_IN'))
