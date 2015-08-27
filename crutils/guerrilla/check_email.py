from trh.guerrilla.base_api_func import BaseAPIFunc


class CheckEmail(BaseAPIFunc):

    """API function: `check_email`.

    Check for new email on the server. Returns a list of the newest messages.
    The maximum size of the list is 20 items.
    The client should not check email too many times as to not overload the
    server.
    Do not check if the email expired, the email checking routing should pause
    if the email expired.
    """
    def __init__(self, session):
        super(CheckEmail, self).__init__(session, 'check_email', 'GET')

    """
    Args:
        - `last_email_id`: The sequence number (id) of the oldest email.
    """
    def execute(self, last_email_id):
        return super(CheckEmail, self).execute(params={
            'seq': last_email_id
        })

    def _get_email_user(self, email):
        md = search(r"(.+)@(.+)", email)
        if not (md is None or md.group(1) is None):
            warn("Giving a full email address instead of just the email user.")
            email = md.group(0)
        return email
