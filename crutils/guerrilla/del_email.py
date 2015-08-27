from trh.guerrilla.base_api_func import BaseAPIFunc


class DelEmail(BaseAPIFunc):

    """API function: `del_email`.

    Delete the emails from the server.
    """
    def __init__(self, session):
        super(DelEmail, self).__init__(session, 'del_email', 'POST')

    """
    Args:
        - `email_ids`: Identifiers of emails to be deleted.
    """
    def execute(self, email_ids=[]):
        return super(DelEmail, self).execute(params={
            'email_ids': email_ids
        })
