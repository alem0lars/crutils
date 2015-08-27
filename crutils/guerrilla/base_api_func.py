from trh.net import get_ip_address, get_user_agent
from trh.log import error, info


class BaseAPIFunc(object):

    """The base class for Guerrilla API functions.
    For more details, see: https://www.guerrillamail.com/GuerrillaMailAPI.html
    """
    def __init__(self, session, func_name, req_type):
        super(BaseAPIFunc, self).__init__()
        self.session = session
        self.api_url = 'http://api.guerrillamail.com/ajax.php'
        self.func_name = func_name
        self.req_type = req_type

    """Execute the API function.
    Args:
        - `params`: The function parameters to be sent.
    Returns:
        The response object (class: `requests.Response`). For more details, see:
        http://www.python-requests.org/en/latest/api/#requests.Response).
    """
    def execute(self, params={}):
        payload = params.copy()
        payload.update({
            'f': self.func_name,
            'ip': '127.0.0.1',
            'agent': get_user_agent()
        })
        payload = {k: v for k, v in payload.items() if v} # Remove empty items.

        info('Performing Guerrilla API function: `%s`' % (self.func_name,))
        if  'PHPSESSID' in self.session.cookies:
            info('Reusing existing session: %s' % (self.session.cookies['PHPSESSID'],))

        if self.req_type == 'GET':
            return self.session.get(self.api_url, params=payload)
        elif self.req_type == 'POST':
            return self.session.post(self.api_url, data=payload)
        else:
            error('Invalid `req_type` argument: %s. Must be `GET` or `POST`' %
                  (self.req_type,))
