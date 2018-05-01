class NMS:
    """  2600hz Kazoo NMS API.

        :param rest_request: The request client to use.
            (optional, default: pyunms.RestRequest())
        :type rest_request: pyunms.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_nmss(self, filters=None):
        """ Get all NMS for an Account.

        :param account_id: ID of Account to get nmss for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('nmss', filters)

    def get_nms_connection(self, filters=None):
        """ Get a specific NMS for an Account.

        :param account_id: ID of Account to get nmss for.
        :param nms_id: ID of the Device to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type nms_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('nms/connection', filters)


    def authorize_nms(self, nms_id, data):
        """ Authorize a Device

        :param account_id: ID of Account to create nms for.
        :param data: Kazoo Device data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('nmss/' + str(nms_id) +
                                      '/authorize', data)

    def restart_nms(self, nms_id, data):
        """ Reboot a Device

        :param account_id: ID of Account to create nms for.
        :param data: Kazoo Device data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('nmss/' + str(nms_id) +
                                      '/restart', data)

