import math
import sys
from colorama import Fore

def main():
	try:
		if sys.argv[1] == "--hide":
			unitoascii(sys.argv[2])

	except:
		pass

def unitoascii(message):
	try:
		vide = []
		for x in message:
			vide.append(ord(x))

		encode = []
		for x in vide:
			enc = (x+5)/(2*5)*(3+2)/(12-5)
			encode.append(enc)

		print(f"{Fore.RED}[Encoded]: " + " | ".join([str(x) for x in encode]))

		decode = []
		for x in encode:
			dec = x*14-5
			a = chr(math.trunc(dec))
			decode.append(a)
		
		for x in decode:
			print(f"{Fore.GREEN}[Decoded]: " + "".join(decode))
			break

	except:
		pass
		
main()
