import pyunms.restrequest
from pyunms.authentication import Authentication
from pyunms.devices import Devices
from pyunms.sites import Sites
from pyunms.nms import NMS
from pyunms.backups import Backups


class PyUNMSClient:
    """ PyUNMSClient is used to access the various API objects. It allows
        state, such as API urls and authentication tokens, to be easily shared
        between the various API objects without the API consumer needing
        to manage them.

        :param api_url: The root URL that the API client should use (example:
                        https://localhost/v2)
        :param rest_request: The request client to use.
            (optional, default: pyunms.restrequest.RestRequest)
        :type api_url: str
        :type rest_request: pyunms.restrequest.RestRequest
    """

    def __init__(self, api_url, rest_request=None):
        self._rest_request = rest_request

        if self._rest_request is None:
            self._rest_request = pyunms.restrequest.RestRequest(api_url)

        self.authentication = Authentication(self._rest_request)
        """ Instance of :class:`pyunms.authentication.Authentication`"""

        self.devices = Devices(self._rest_request)
        """ Instance of :class:`pyunms.devices.Devices`"""

        self.sites = Sites(self._rest_request)
        """ Instance of :class:`pyunms.users.Sites`"""

        self.nms = NMS(self._rest_request)
        """ Instance of :class:`pyunms.users.Sites`"""

        self.backups = Backups(self._rest_request)
        """ Instance of :class:`pykazoo.backups.Backups`"""