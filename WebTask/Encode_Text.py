import hashlib
import hmac
import base64

def getSign(xDate, AppKey):
    HmacText = hmac.new(AppKey.encode("UTF-8"), xDate.encode("UTF-8"), hashlib.sha1).digest()
    HmacText = base64.b64encode(HmacText)
    return HmacText.decode()