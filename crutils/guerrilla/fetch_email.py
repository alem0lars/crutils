from trh.guerrilla.base_api_func import BaseAPIFunc


class FetchEmail(BaseAPIFunc):

    """API function: `fetch_email`.

    Get the contents of an email.
    Notes:
        - All HTML in the body of the email is filtered, i.e. Javascript,
          applets, iframes, etc is removed.
        - Subject and email excerpt are escaped using HTML Entities.
        - Only emails owned by the current session id can be fetched.
        - All images in the email are relative to
          `http://www.guerrillamail.com/res.php` - this script will generate a
          'blocked by GM' image, indicating that the image was blocked.
          The CGI parameters for this script are as follows:
          r: Is it a resource? 1 if true. Always 1
          n: Node. The element type. Can be a string of letters (a-z)
          q: The query string for the original image. This is URL Encoded
    """
    def __init__(self, session):
        super(FetchEmail, self).__init__(session, 'fetch_email', 'GET')

    """
    Args:
        - `email_id`: The id of the email to fetch.
    """
    def execute(self, email_id):
        return super(FetchEmail, self).execute(params={
            'email_id': email_id
        })
