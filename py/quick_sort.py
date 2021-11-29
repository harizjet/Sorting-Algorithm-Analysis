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

	# algo start
	def pivot(array, st, ed):
		piv_i = math.floor((ed-st)/2)+st 
		piv = array[piv_i]
		il, ir = st, ed

		while il < ir:
			while ((array[il] <= piv or il == piv_i) and il < ed):
				il += 1
			while ((array[ir] >= piv or ir == piv_i) and ir > st):
				ir -= 1
			if il < ir:
				array[il], array[ir] = array[ir], array[il]

		if ir < piv_i < il:
			return piv_i
		elif piv_i >= il:
			array[piv_i], array[il] = array[il], array[piv_i]
			return il
		else:
			array[piv_i], array[ir] = array[ir], array[piv_i]
			return ir

	def quicksort(array, st, ed):
		if st < ed:
			i = pivot(array, st, ed)

			quicksort(array, st, i-1)
			quicksort(array, i+1, ed)

	_start = time.time()
	quicksort(array, 0, array_n-1)
	_end = time.time()

	with open(f"./result/py.txt", "a") as f:
		f.write(f"quick_sort, {direc}, {_end - _start}\n")