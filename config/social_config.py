import os

AUTHENTICATION_BACKENDS = (
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")

if os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_EMAILS"):
    SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_EMAILS = os.environ.get(
        "SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_EMAILS"
    ).split(",")

if os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS"):
    SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS = os.environ.get(
        "SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS"
    ).split(",")

SOCIAL_AUTH_REDIRECT_URI = os.environ.get("SOCIAL_AUTH_REDIRECT_URI")