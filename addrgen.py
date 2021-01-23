from bs4 import BeautifulSoup
import sys
import requests
from colorama import Fore

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
	sites = [
	'https://www.fakeaddressgenerator.com/US_Real_Random_Address', 
	'https://www.fakeaddressgenerator.com/UK_Real_Random_Address', 
	'https://www.fakeaddressgenerator.com/Canada_Real_Random_Address', 
	'https://www.fakeaddressgenerator.com/AU_Real_Random_Address', 
	'https://www.fakeaddressgenerator.com/usa_address_generator', 
	'https://www.fakeaddressgenerator.com/World/ca_address_generator', 
	'https://www.fakeaddressgenerator.com/World/uk_address_generator', 
	'https://www.fakeaddressgenerator.com/World/au_address_generator', 
	'https://www.fakeaddressgenerator.com/World/Germany_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Algeria', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Albania', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Armenia', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Argentina', 
	'https://www.fakeaddressgenerator.com/World/au_address_generator', 
	'https://www.fakeaddressgenerator.com/World/Austria_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Azerbaijan', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Barbados', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Bangladesh', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Bahrain', 
	'https://www.fakeaddressgenerator.com/World/Belgium_address_generator', 
	'https://www.fakeaddressgenerator.com/World_more/Belarus_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Brunei', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Bolivia', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Bahamas', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Botswana', 
	'https://www.fakeaddressgenerator.com/World/Brazil_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Cayman', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Chile', 
	'https://www.fakeaddressgenerator.com/World_more/china_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Cambodia', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Cameroon', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Colombia', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Croatia', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Costa Rica', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Cuba', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Cyprus', 
	'https://www.fakeaddressgenerator.com/World/Czech_address_generator', 
	'https://www.fakeaddressgenerator.com/World/Denmark_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Dominican Republic', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/DR Congo', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Ecuador', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/El Salvador', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Egypt', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Emirates', 
	'https://www.fakeaddressgenerator.com/World/Estonia_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Ethiopia', 
	'https://www.fakeaddressgenerator.com/World/Finland_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Fiji', 
	'https://www.fakeaddressgenerator.com/World/France_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Gabon', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Georgia', 
	'https://www.fakeaddressgenerator.com/World/Germany_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Ghana', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Guatemala', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Hongkong', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Honduras', 
	'https://www.fakeaddressgenerator.com/World/Hungary_address_generator', 
	'https://www.fakeaddressgenerator.com/World/Iceland_address_generator', 
	'https://www.fakeaddressgenerator.com/World_more/India_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Indonesia', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Ireland', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Israel', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Iran', 
	'https://www.fakeaddressgenerator.com/World/Italy_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Ivory Coast', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Jamaica', 
	'https://www.fakeaddressgenerator.com/World_more/Japan_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Jordan', 
	'https://www.fakeaddressgenerator.com/World_more/kazakhstan_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Kenya', 
	'https://www.fakeaddressgenerator.com/World_more/Korea_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Kyrgyzstan', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Kuwait', 
	'https://www.fakeaddressgenerator.com/World_more/Latvia_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Lebanon', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Sri Lanka', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Lesotho', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Lithuania', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Luxembourg', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Libya', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Morocco', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Madagascar', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Mali', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Myanmar', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Malta', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Mauritius', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Malawi', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Mexico', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Malaysia', 
	'https://www.fakeaddressgenerator.com/World_more/Moldova_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Namibia', 
	'https://www.fakeaddressgenerator.com/World/New_Zealand_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Nigeria', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Nicaragua', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Nepal', 
	'https://www.fakeaddressgenerator.com/World/Netherlands_address_generator', 
	'https://www.fakeaddressgenerator.com/World/Norway_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Oman', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Panama', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Peru', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Papua New Guinea', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Philippines', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Pakistan', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Puerto Rico', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Paraguay', 
	'https://www.fakeaddressgenerator.com/World/Poland_address_generator', 
	'https://www.fakeaddressgenerator.com/World/Portugal_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Qatar', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Romania', 
	'https://www.fakeaddressgenerator.com/World_more/Russia_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Rwanda', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Saudi Arabia', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Singapore', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Slovakia', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Senegal', 
	'https://www.fakeaddressgenerator.com/World/Spain_address_generator', 
	'https://www.fakeaddressgenerator.com/World_more/Slovenia_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Suriname', 
	'https://www.fakeaddressgenerator.com/World_more/South_Africa_address_generator', 
	'https://www.fakeaddressgenerator.com/World_more/Sweden_address_generator', 
	'https://www.fakeaddressgenerator.com/World_more/Switzerland_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Syria', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Thailand', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Turkey', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Trinidad and Tobago', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Taiwan', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Tanzania', 
	'https://www.fakeaddressgenerator.com/World_more/Tunisia_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Uganda', 
	'https://www.fakeaddressgenerator.com/World_more/Ukraine_address_generator', 
	'https://www.fakeaddressgenerator.com/World_more/Uruguay_address_generator', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Uzbekistan', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Venezuela', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Vietnam', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Yemen', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Zambia', 
	'https://www.fakeaddressgenerator.com/All_countries/address/country/Zimbabwe']
	try:
		if country == "FR":
			client = {"__cfduid":"d2621dc544d7cac81c51b84e6db444fe81611369636"}
			req = requests.get(sites[0], cookies=client)
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

		elif country == "DZ":
			client = {"__cfduid":"d2621dc544d7cac81c51b84e6db444fe81611369636"}
			req = requests.get(sites[1], cookies=client)
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
