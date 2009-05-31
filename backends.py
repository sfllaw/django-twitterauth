from models import User
from oauth import oauth

class TwitterBackend(object):
    """
    Authenticates against twitter.
    """
    def authenticate(self, key=None, secret=None):
        token = oauth.OAuthToken(key, secret)
        try:
            user = User.objects.get(key=key, secret=secret)
            if user.is_twauthorized():
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
