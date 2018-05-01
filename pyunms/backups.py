class Backups:
    """  2600hz Kazoo Backups API.
        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_all_backup(self, device_id, filters=None):
        """ Get all Backups for an Account.
        :param device_id: ID of Account to get devices for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type device_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('devices/' + str(device_id) +
                                     '/backup', filters)

    def get_backup(self, device_id, backup_id, filters=None):
        """ Get Backups for an Account.
        :param device_id: ID of Account to get devices for.
        :param backup_id: ID of the Backups to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type device_id: str
        :type backup_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('devices/' + str(device_id) +
                                     '/backups/' + str(backup_id), filters)

    def create_backup(self, device_id):
        """ Create Backups
        :param device_id: ID of Account to create Backups for.
        :param data: Kazoo Backups data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type device_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('devices/' + str(device_id) +
                                     '/backups')

    def apply_backup(self, device_id, backup_id):
        """ apply Backups
        :param device_id: ID of Account to apply Backups for.
        :param data: Kazoo Backups data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type device_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('devices/' + str(device_id) +
                                     '/backups/' + str(backup_id) + '/apply')
                                     
    def update_backup(self, device_id, backup_id, data):
        """ Updates Backups
        :param device_id: ID of Account to update Backups for.
        :param backup_id: ID of Backups to update.
        :param data: Kazoo Account data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type device_id: str
        :type backup_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('devices/' + str(device_id) +
                                      '/backups/' + str(backup_id), data)

    def delete_backup(self, device_id, backup_id):
        """ Deletes Backups
        :param device_id: ID of Account to delete Backups from.
        :param backup_id: ID of Device to delete.
        :return: Kazoo Data (see official API docs).
        :type device_id: str
        :type backup_id: str
        :rtype: dict
        """
        return self.rest_request.delete('devices/' + str(device_id) +
                                        '/backups/' + str(backup_id))

    def get_raw_backup(self, device_id, backup_id, filters=None):
        """ Get Raw Backups for an Account.
        :param device_id: ID of Account to get devices for.
        :param backup_id: ID of the Backups to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type device_id: str
        :type backup_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('devices/' + str(device_id) +
                                     '/backups/' + str(backup_id) ,
                                     filters)

    def update_raw_backup(self, device_id, data):
        """ Update Raw Backups for an Account.
        :param device_id: ID of Account to get devices for.
        :param backup_id: ID of the Backups to get.
        :return: Kazoo Data (see official API docs).
        :type device_id: str
        :type backup_id: str
        :rtype: dict
        """
        return self.rest_request.put('devices/' + str(device_id) +
                                      '/backups',
                                      data, "'Content-disposition', 'application/octet-stream; name=\"uploadedfile\"'")