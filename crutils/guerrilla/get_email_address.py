from trh.guerrilla.base_api_func import BaseAPIFunc


class GetEmailAddress(BaseAPIFunc):

    """API function: `get_email_address`.

    The function is used to initialize a session and set the client with an
    email address.
    If the session already exists, then it will return the email address details
    of the existing session.
    If a new session needs to be created, then it will first check for the
    `SUBSCR` cookie to create a session for a subscribed address, otherwise it
    will create new email address randomly.
    The session is maintained using HTTP Cookies.
    The cookie name is `PHPSESSID`, and it will be given in the resulting HTTP
    header.
    The client should always store this cookie and send it whenever making an
    API call. A new session will be created when the `PHPSESSID` cookie is not
    given by the client.
    The function also generates a new welcome email for the user.
    """
    def __init__(self, session):
        super(GetEmailAddress, self).__init__(session, 'get_email_address', 'GET')

    def execute(self):
        return super(GetEmailAddress, self).execute(params={'lang': 'en'})
