from trh.guerrilla.base_api_func import BaseAPIFunc


class Extend(BaseAPIFunc):

    """API function: `extend`.

    Extend the email address time by 1 hour.
    A maximum of 2 hours can be extended.
    """
    def __init__(self, session):
        super(Extend, self).__init__(session, 'extend', 'POST')
