import requests
import ssl
import sys
from http.cookiejar import MozillaCookieJar
from coursera.coursera_dl import main

class CustomTLSAdapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.set_ciphers('ECDHE+AESGCM:ECDHE+CHACHA20:ECDHE+AES')
        kwargs['ssl_context'] = context
        return super(CustomTLSAdapter, self).init_poolmanager(*args, **kwargs)

def custom_get_session():
    """
    Create a session with TLS v1.2 certificate
    """
    session = requests.Session()
    cj = MozillaCookieJar('cookies.txt')
    try:
        cj.load(ignore_discard=True, ignore_expires=True)
    except (IOError, OSError):
        pass
    session.cookies = cj
    session.mount('https://', CustomTLSAdapter())
    return session

if __name__ == "__main__":
    session = custom_get_session()
    sys.exit(main())
