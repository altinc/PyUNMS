import hashlib


class Authentication:
    """ Authenticates against the 2600hz Kazoo API.

        :param rest_request: The request client to use.
            (optional, default: pyunms.RestRequest())
        :type rest_request: pyunms.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def api_auth(self, api_key):
        """ Authenticate using an API Key.

        Sets the Auth Token for future KazooClientAPI calls as a side affect.

        :param api_key: API Key to authenticate with.
        :return: Kazoo Data (see official API docs)
        :type api_key: str
        :rtype: dict
        """
        data = self.rest_request.put('api_auth',
                                     {'data': {'api_key': api_key}})

        self.rest_request.auth_token = data['auth_token']
        self.rest_request.account_id = data['data']['account_id']

        return data

    def user_auth(self, username, password):
        """ Authenticate using a Username, Password and Account Name.

        Sets the Auth Token for future KazooClientAPI calls as a side affect.

        :param username: Username to use.
        :param password: Password to use.
        :param account_name: Account Name to use.
        :return: Kazoo Data (see official API docs)
        :type username: str
        :type password: str
        :type account_name: str
        :rtype: dict
        """
        combined_encoded = (username + ':' + password).encode('utf-8')
        credentials = hashlib.md5(combined_encoded).hexdigest()
        data = self.rest_request.post('user/login',
                                     {'username': username,
                                               'password': password, 'sessionTimeout':'36000000'})
        self.rest_request.auth_token = data['x-auth-token']
        #self.rest_request.account_id = data['data']['account_id']

        return data

    @property
    def authenticated(self):
        """ Checks whether or not the auth token has already been retrieved.
        This is useful for rate limiting auth requests, which can be costly.

        :return: Whether or not the auth token has already been retrieved.
        :rtype: bool
        """

        return self.rest_request.auth_token is not None

    @property
    def account_id(self):
        """ Gets the ID of the account used for authentication.
        :return: ID of the account used for authentication.
        :rtype: str
        """

        return self.rest_request.account_id
