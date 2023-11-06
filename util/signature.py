import hmac
import hashlib

orgHost = 'picacomic.com'
BaseUrl = "https://picaapi." + orgHost + "/"


def getNonce():
    return "bebp53hty6z7kwjyxhyjywjszpwrwtbi"


def getsignature(url, ts, method):
    """
    function getsignature(url, ts, method) {
        var raw = url.replace(BaseUrl, "") + ts + getNonce() + method + appleKillFlag;
        raw = raw.toLowerCase();
        return CryptoJS.HmacSHA256(raw, appleVerSion).toString(CryptoJS.enc.Hex);
    }
    """

    appleKillFlag = "C69BAF41DA5ABD1FFEDC6D2FEA56B"
    raw = (url + ts + getNonce() + method + appleKillFlag).lower()
    secretKey = "~d}$Q7$eIni=V)9\RK/P.RM4;9[7|@/CA}b~OW!3?EV`:<>M7pddUBL5n|0/*Cn"  # Replace with your actual secret key
    signature = hmac.new(secretKey.encode('utf-8'), raw.encode('utf-8'), hashlib.sha256).hexdigest()
    return signature


def test_getsignature():
    url = "users/punch-in"
    ts = "1699282517"
    method = "POST"
    expected_signature = "a2bcc6539cc9a1f7751bd0eaa5382a54153c516c04fa12c9b0336f4105d03487"
    signature = getsignature(url, ts, method)
    print("True", expected_signature)
    print("Mine", signature)

    assert signature == expected_signature, "Test failed: Signature does not match the expected value."


if __name__ == "__main__":
    test_getsignature()
    print("Test passed: Signature matches the expected value.")
