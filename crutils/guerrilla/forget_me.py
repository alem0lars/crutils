from trh.guerrilla.base_api_func import BaseAPIFunc


class ForgetMe(BaseAPIFunc):

    """API function: `forget_me`.

    Forget the current email address.
    This will not stop the session, the existing session will be maintained.
    A subsequent call to `get_email_address` will fetch a new email address or
    the client can call `set_email_user` to set a new address.
    Typically, a user would want to set a new address manually after clicking
    the forget me button.
    """
    def __init__(self, session):
        super(ForgetMe, self).__init__(session, 'forget_me', 'POST')

    """
    Args:
        - `email_addr`: The email address to forget.
    """
    def execute(self, email_id):
        return super(ForgetMe, self).execute(params={
            'email_addr': email_addr
        })
