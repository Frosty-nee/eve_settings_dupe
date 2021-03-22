#! python

import os
import sys
import shutil

CHAR_LIST = {
	"frosty-nee":	92301442,
	"moon":			94145863,
	"frostynee":	92489088,
	"mohawk":		94955933,
	"ariadne":		93471424,
	"catherine":	96476105,
	"anya": 		92776702,
	"corinne":		96109765,
	"iwhipmycyno": 	93508210,
	"valerie":	2112226739,
	"shewhothirsts":2118461359,
}



if __name__ == "__main__":
	print(sys.argv)
	if len(sys.argv) == 1:
		print("./duplicate_settings.py from to")
		exit()
	if sys.argv[1] == 'list':
		for k in CHAR_LIST.keys():
			print(k)
		exit()
	copy_to = []
	copy_from = CHAR_LIST[sys.argv[1]]
	if sys.argv[2] == 'all':
		for _,v in CHAR_LIST.items():
			if v != CHAR_LIST[sys.argv[1]]:
				copy_to.append(v)
	else:
		for entry in sys.argv[2:]:
			if entry in CHAR_LIST.keys() and entry != sys.argv[1]:
				copy_to.append(CHAR_LIST[entry])
			print(copy_to)
	copy_from = 'core_char_{}.dat'.format(copy_from)
	for entry in copy_to:
		try:
			os.remove('core_char_{}.dat'.format(entry))
		except Exception e:
			print(e)
		shutil.copyfile(copy_from, 'core_char_{}.dat'.format(entry))
