"""Configure and hold all pertinent security information for the app."""
import os
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Authenticated
from pyramid.security import Allow
from passlib.apps import custom_app_context as pwd_context
from pyramid.session import SignedCookieSessionFactory  # <-- include this


class MyRoot(object):
    """My root class."""

    def __init__(self, request):
        """Init auth class."""
        self.request = request

    __acl__ = [
        (Allow, Authenticated, 'secret'),
    ]


def is_authenticated(username, password):
    """Check if the user's username and password are good."""
    if username == os.environ.get('AUTH_USERNAME', ''):
        if pwd_context.verify(password, os.environ.get('AUTH_PASSWORD', '')):
            return True
    return False


def includeme(config):
    """."""
    # set up authentication
    auth_secret = os.environ.get('AUTH_SECRET', '')
    authn_policy = AuthTktAuthenticationPolicy(
        secret=auth_secret,
        hashalg='sha512'
    )
    config.set_authentication_policy(authn_policy)

    # set up authorization
    authz_policy = ACLAuthorizationPolicy()
    config.set_authorization_policy(authz_policy)
    # config.set_default_permission('secret')
    # if i want every view by default to be behind a login wall
    config.set_root_factory(MyRoot)

    # set up CSRF token to prevent CSRF attack
    session_secret = os.environ.get('SESSION_SECRET', '')
    session_factory = SignedCookieSessionFactory(session_secret)
    config.set_session_factory(session_factory)
    config.set_default_csrf_options(require_csrf=True)
