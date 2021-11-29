import math
import sys
import time


if __name__ == "__main__":
	
	direc = sys.argv[1]

	with open(f"./data/{direc}.txt", "r") as f:
		txt = f.read()
	
	# txt = None
	if not txt:
		txt = input()

	array = [int(x.strip()) for x in txt.split(',')]

	array_n = len(array)

	# algo start
	def countsort(arr, exp):
		n = len(arr)

		out = [0] * n
		count = [0] * (10)
		for i in range(n):
			ind = arr[i] // exp
			count[ind%10] += 1

		for i in range(1, 10):
			count[i] += count[i - 1]

		i = n - 1
		while i >= 0:
			ind = arr[i] // exp
			out[count[ind % 10] - 1] = arr[i]
			count[ind % 10] -= 1
			i -= 1

		for i in range(len(arr)):
			arr[i] = out[i]

	def radixsort(arr):
		m = max(arr)

		exp = 1
		while m / exp > 0:
			countsort(arr, exp)
			exp *= 10

	_start = time.time()
	radixsort(array)
	_end = time.time()

	with open(f"./result/py.txt", "a") as f:
		f.write(f"radix_sort, {direc}, {_end - _start}\n")