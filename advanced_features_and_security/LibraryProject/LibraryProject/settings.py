bookshelf.CustomUser
AUTH_USER_MODEL = 'relationship_app.CustomUser'
import os
DEBUG = False  # Set to False in production
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
INSTALLED_APPS += ['csp']

CSP_DEFAULT_SRC = ("'self'",)  
CSP_SCRIPT_SRC = ("'self'",)  
ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']
SECURE_BROWSER_XSS_FILTER = True  # Enable browser's XSS filter
X_FRAME_OPTIONS = 'DENY'  # Prevent iframe embedding
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent browser MIME-sniffing
Use secure cookies
CSRF_COOKIE_SECURE = True  # Ensure CSRF cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True  # Ensure session cookies are only sent over HTTPS

CSP_DEFAULT_SRC = ("'self'",)  # Default policy restricting content to same-origin
SECURE_SSL_REDIRECT = True 
SECURE_HSTS_SECONDS = 3600 
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

