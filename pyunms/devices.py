class Devices:
    """  2600hz Kazoo Devices API.

        :param rest_request: The request client to use.
            (optional, default: pyunms.RestRequest())
        :type rest_request: pyunms.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_devices(self, filters=None):
        """ Get all Devices for an Account.

        :param account_id: ID of Account to get devices for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('devices', filters)

    def get_device(self, device_id, filters=None):
        """ Get a specific Devices for an Account.

        :param account_id: ID of Account to get devices for.
        :param device_id: ID of the Device to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type device_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('devices/' + str(device_id), filters)

    def create_device(self, data):
        """ Create a Device

        :param account_id: ID of Account to create device for.
        :param data: Kazoo Device data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.put('devices', data)

    def update_device(self, device_id, data):
        """ Updates a Device

        :param account_id: ID of Account to update device for.
        :param device_id: ID of Device to update.
        :param data: Kazoo Account data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type device_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/devices/' + str(device_id), data)

    def delete_device(self, device_id):
        """ Deletes a Device

        :param account_id: ID of Account to delete device from.
        :param device_id: ID of Device to delete.
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type device_id: str
        :rtype: dict
        """
        return self.rest_request.delete('accounts/' + str(account_id) +
                                        '/devices/' + str(device_id))

    def get_devices_status(self, filters=None):
        """ Gets Devices Status

        :param account_id: ID of Account to get device statuses for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('devices/status', filters)

    def authorize_device(self, device_id, data):
        """ Authorize a Device

        :param account_id: ID of Account to create device for.
        :param data: Kazoo Device data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('devices/' + str(device_id) +
                                      '/authorize', data)

    def restart_device(self, device_id):
        """ Reboot a Device

        :param account_id: ID of Account to create device for.
        :param data: Kazoo Device data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('devices/' + str(device_id) +
                                      '/restart')

