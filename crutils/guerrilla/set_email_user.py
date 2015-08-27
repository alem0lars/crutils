from re import search
from trh.guerrilla.base_api_func import BaseAPIFunc
from trh.log import warn


class SetEmailUser(BaseAPIFunc):

    """API function: `set_email_user`.

    Set the email address to a different email address.
    If the email address is a subscriber, then return the subscription details.
    If the email is not a subscriber, then the email address will be given 60
    minutes again.
    A new email address will be generated if the email address is not in the
    database and a welcome email message will be generated.
    """
    def __init__(self, session):
        super(SetEmailUser, self).__init__(session, 'set_email_user', 'POST')

    """
    Args:
        - `email`: The email username to be set. If a full email address is
                   given, the domain part will be ignored.
    """
    def execute(self, email):
        return super(SetEmailUser, self).execute(params={
            'lang': 'en',
            'email_user': self._get_email_user(email)
        })

    def _get_email_user(self, email):
        md = search(r"(.+)@(.+)", email)
        if not (md is None or md.group(1) is None):
            warn("Giving a full email address instead of just the email user.")
            email = md.group(0)
        return email
