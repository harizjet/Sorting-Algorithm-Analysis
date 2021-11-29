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
	for i in range(array_n-1):
		for ir in range(i, array_n):
			if array[ir] < array[i]:
				array[ir], array[i] = array[i], array[ir]
	_end = time.time()

	with open(f"./result/py.txt", "a") as f:
		f.write(f"selection_sort, {direc}, {_end - _start}\n")