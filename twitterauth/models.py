import datetime
from oauth import oauth
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from twitterauth.twitter import TwitterAPI


class User(models.Model):

    SEX_MALE = 0
    SEX_FEMALE = 1
    SEX_CHOICES = (
        (SEX_MALE, _('Male')),
        (SEX_FEMALE, _('Female')),
    )

    username = models.CharField(max_length=40)
    email = models.EmailField()

    last_login = models.DateTimeField(_('last login'), default=datetime.datetime.now)
    date_joined = models.DateTimeField(_('date joined'), default=datetime.datetime.now)

    key = models.CharField(max_length=200)
    secret = models.CharField(max_length=200)

    sex = models.SmallIntegerField(choices=SEX_CHOICES, default=0)
    weight = models.SmallIntegerField(default=160)

    @property
    def bac(self):
        return bac.bac(self.empties.all(), self.weight, self.sex)

    def __unicode__(self):
        return self.username

    _twitter_api = None
    @property
    def twitter_api(self):
        if self._twitter_api is None:
            self._twitter_api = TwitterAPI(self)
        return self._twitter_api

    def get_absolute_url(self):
        return reverse('user', kwargs={'id': self.id})

    def to_string(self, only_key=False):
        # so this can be used in place of an oauth.OAuthToken
        if only_key:
            return urllib.urlencode({'oauth_token': self.key})
        return urllib.urlencode({'oauth_token': self.key, 'oauth_token_secret': self.secret})

    def get_and_delete_messages(self): pass

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_authorized(self): 
        return True

    def is_twauthorized(self):
        return bool(self.twitter_api.verify_credentials())

    def tweet(self, status):
        return api(
            'https://twitter.com/statuses/update.json',
            self.token(),
            http_method='POST',
            status=status
        )


class AnonymousUser(object):
    username = ''
    
    key = ''
    secret = ''

    def __unicode__(self):
        return 'AnonymousUser'

    def to_string(self, only_key=False):
        raise NotImplementedError

    _twitter_api = None
    @property
    def twitter_api(self):
        if self._twitter_api is None:
            self._twitter_api = TwitterAPI()
        return self._twitter_api

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return 1 # instances always return the same hash value

    def save(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    def tweet(self, status):
        raise NotImpelementedError

    def is_anonymous(self):
        return True

    def is_authenticated(self):
        return False

    def is_twauthorized(self):
        return False
