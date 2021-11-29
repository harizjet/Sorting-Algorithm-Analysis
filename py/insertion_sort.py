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
	for i in range(1, array_n):
		for il in range(i-1, -1, -1):
			if array[il+1] > array[il]:
				break
			array[il], array[il+1] = array[il+1], array[il]
	_end = time.time()

	with open(f"./result/py.txt", "a") as f:
		f.write(f"insertion_sort, {direc}, {_end - _start}\n")