from bs4 import BeautifulSoup
import sys
import requests
from colorama import Fore
import json

def main():
	try:
		if sys.argv[1] == "--person":
			person(sys.argv[2])

		elif sys.argv[1] == "--getlinks":
			getlinks()

	except:
		pass

def getlinks():
	req = requests.get("https://www.fakeaddressgenerator.com/All_countries/address/country/Algeria#all-countries")
	soup = BeautifulSoup(req.text, 'html.parser')
	vide = []
	for a in soup.find_all('a', href=True):
		sites = "https://www.fakeaddressgenerator.com" + a['href']
		vide.append(sites)
	print(vide)

def person(country):
	countries = ['https://www.fakeaddressgenerator.com/World/France_address_generator', 'https://www.fakeaddressgenerator.com/All_countries/address/country/Algeria']
	try:
		if country == "FR":
			client = {"__cfduid":"d2621dc544d7cac81c51b84e6db444fe81611369636"}
			req = requests.get(countries[0], cookies=client)
			soup = BeautifulSoup(req.text, 'html.parser')
			grab = soup.find_all(attrs={"type":"text"})
			arr = [str(x) for x in grab]
			vide = []
			for i in arr:
				vide.append(i)

			print(f"{Fore.YELLOW}[Full Name]: " + f"{Fore.GREEN}" + vide[1].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")
			print(f"{Fore.YELLOW}[Gender]: " + f"{Fore.GREEN}" + vide[2].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")
			print(f"{Fore.YELLOW}[Title]: " + f"{Fore.GREEN}" + vide[3].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")
			print(f"{Fore.YELLOW}[Birthday]: " + f"{Fore.GREEN}" + vide[4].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")
			print(f"{Fore.YELLOW}[Social Security Number]: " + f"{Fore.GREEN}" + vide[5].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")
			print(f"{Fore.YELLOW}[Street]: " + f"{Fore.GREEN}" + vide[6].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")
			print(f"{Fore.YELLOW}[City]: " + f"{Fore.GREEN}" + vide[7].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")
			print(f"{Fore.YELLOW}[State Full]: " + f"{Fore.GREEN}" + vide[8].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")
			print(f"{Fore.YELLOW}[Zip Code]: " + f"{Fore.GREEN}" + vide[9].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")
			print(f"{Fore.YELLOW}[Phone Number]: " + f"{Fore.GREEN}" + vide[10].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")

		elif country == 'DZ':
			client = {"__cfduid":"d2621dc544d7cac81c51b84e6db444fe81611369636"}
			req = requests.get(countries[1], cookies=client)
			soup = BeautifulSoup(req.text, 'html.parser')
			grab = soup.find_all(attrs={"type":"text"})
			arr = [str(x) for x in grab]
			vide = []
			for i in arr:
				vide.append(i)

			print(f"{Fore.YELLOW}[Full Name]: " + f"{Fore.GREEN}" + vide[1].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")
			print(f"{Fore.YELLOW}[Gender]: " + f"{Fore.GREEN}" + vide[2].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")
			print(f"{Fore.YELLOW}[Title]: " + f"{Fore.GREEN}" + vide[3].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")
			print(f"{Fore.YELLOW}[Birthday]: " + f"{Fore.GREEN}" + vide[4].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")
			print(f"{Fore.YELLOW}[Social Security Number]: " + f"{Fore.GREEN}" + vide[5].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")
			print(f"{Fore.YELLOW}[Street]: " + f"{Fore.GREEN}" + vide[6].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")
			print(f"{Fore.YELLOW}[City]: " + f"{Fore.GREEN}" + vide[7].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")
			print(f"{Fore.YELLOW}[State Full]: " + f"{Fore.GREEN}" + vide[8].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")
			print(f"{Fore.YELLOW}[Zip Code]: " + f"{Fore.GREEN}" + vide[9].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")
			print(f"{Fore.YELLOW}[Phone Number]: " + f"{Fore.GREEN}" + vide[10].split('value="')[1].replace('"/>', '') + f"{Fore.RESET}")																																																																								
	except:
		pass

main()
