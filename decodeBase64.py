import base64


def decodeBase64(data):
    data = data.replace(" ", "")
    validcharset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    for i in data:
        if i != validcharset:
            return "Did not decode, invalid characters found in input"
    try:
        if "str" not in str(type(data)):
            data = data.decode()
        missing_padding = len(data) % 4
        if missing_padding != 0:
            data += '=' * (4 - missing_padding)
        return (base64.b64decode(data)).decode()
    except Exception as e:
        return "Did not decode, encounted the following error: " + str(e)


print(
    decodeBase64(input("Enter a base-64 encoded string: \n"))
)
