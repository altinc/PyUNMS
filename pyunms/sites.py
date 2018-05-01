class Sites:
    """  2600hz Kazoo Sites API.

        :param rest_request: The request client to use.
            (optional, default: pyunms.RestRequest())
        :type rest_request: pyunms.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_sites(self, filters=None):
        """ Get all Sites for an Account.

        :param account_id: ID of Account to get Sites for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('sites', filters)

    def get_site(self, site_id, filters=None):
        """ Get a specific Site for an Account.

        :param account_id: ID of Account to get Site for.
        :param site_id: ID of the Site to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type site_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('sites/' + str(site_id), filters)

    def create_site(self, data):
        """ Create a Site

        :param account_id: ID of Account to create Site for.
        :param data: Kazoo Site data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('sites',
                                     data)

    def update_site(self, site_id, data):
        """ Updates a Site

        :param account_id: ID of Account to update Site for.
        :param site_id: ID of Site to update.
        :param data: Kazoo Account data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type site_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('sites/' + str(site_id), data)

    def delete_site(self, site_id):
        """ Deletes a Site

        :param account_id: ID of Account to delete Site from.
        :param site_id: ID of Site to delete.
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type site_id: str
        :rtype: dict
        """
        return self.rest_request.delete('sites/' + str(site_id))
