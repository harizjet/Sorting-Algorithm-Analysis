import math
import sys
import time


if __name__ == "__main__":
	
	direc = sys.argv[1]

	with open(f"./data/{direc}.txt", "r") as f:
		txt = f.read()
	
	if not txt:
		txt = input()

	array = [int(x.strip()) for x in txt.split(',')]

	array_n = len(array)

	_start = time.time()
	# algo start
	found = False
	for i in range(array_n-1, -1, -1):
		for il in range(0, i):
			if array[il] > array[il+1]:
				array[il], array[il+1] = array[il+1], array[il]
				found = True
			if not found: break
	_end = time.time()

	with open(f"./result/py.txt", "a") as f:
		f.write(f"bubble_sort, {direc}, {_end - _start}\n")