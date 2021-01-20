import requests 
from bs4 import BeautifulSoup
import sys
from colorama import Fore
import os
import string

def usage():
	print(f"{Fore.GREEN}[Usage]: python3 fuzz.py -u [url/*.php] -w [wordlist.txt]{Fore.RESET}")

def clear():
	os.system("cls" if os.name == "nt" else "clear")

def main():
	try:
		if sys.argv[1] == "-u" and sys.argv[3] == "-w":
				fuzz(sys.argv[2], sys.argv[4])
		else:
			usage()
			pass
	except:
		usage()
		pass

def fuzz(site, wordlist):
	try:
		clear()
		with open(wordlist, 'r') as file:
			wl = file.readlines()
			wl = [x.strip() for x in wl]
		with requests.session() as s:
			ug = {"__cfduid": "d9158d4877e0623d772a0bbe76a4fbb0e1610165387"}
			for i in wl:	
				req = s.get(site + "?" + i + "=reflect", cookies=ug)
				string = "reflect"
				print(f"{Fore.RED}[Failed]: " + i)
				if string in req.text:
					print("\n" + f"{Fore.GREEN}" + "[Success]: ?" + i + "=" + f"{Fore.RESET}" + "\n")
					break
	except:
		pass

main()
