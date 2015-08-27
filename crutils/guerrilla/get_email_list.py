from trh.guerrilla.base_api_func import BaseAPIFunc


class GetEmailList(BaseAPIFunc):

    """API function: `get_email_list`.

    Gets a maximum of 20 messages from the specified offset.
    Offset of 0 will fetch a list of the first 10 emails, offset of 10 will
    fetch a list of the next 10, and so on.
    This function is useful for populating the initial email list.

    Note:
        When returned, subject and email excerpt are escaped using HTML Entities.
    """
    def __init__(self, session):
        super(GetEmailList, self).__init__(session, 'get_email_list', 'GET')

    """
    Args:
        - `offset`: How many emails to start from (skip). Starts from 0.
        - `seq`: The sequence number(id) of the first email, optional.
    """
    def execute(self, offset, first_email_id=None):
        return super(GetEmailList, self).execute(params={
            'offset': offset,
            'seq': first_email_id
        })

    def _get_email_user(self, email):
        md = search(r"(.+)@(.+)", email)
        if not (md is None or md.group(1) is None):
            warn("Giving a full email address instead of just the email user.")
            email = md.group(0)
        return email
