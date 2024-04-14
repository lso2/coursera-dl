from http.cookiejar import MozillaCookieJar

def prepare_auth_headers(session, include_cauth=True):
    cj = MozillaCookieJar(filename='cookies.txt')
    try:
        cj.load(ignore_discard=True, ignore_expires=True)
    except (IOError, OSError):
        pass

    headers = {}
    if include_cauth:
        cauth = next((cookie for cookie in cj if cookie.name == 'CAUTH'), None)
        if cauth:
            headers['CAUTH'] = cauth.value

    return headers
