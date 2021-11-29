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
	def merge(arr_1, arr_2):
		ans_arr = []
		i1, i2 = 0, 0

		while i1 < len(arr_1) and i2 < len(arr_2):
			if arr_1[i1] < arr_2[i2]:
				ans_arr.append(arr_1[i1])
				i1 += 1
			else:
				ans_arr.append(arr_2[i2])
				i2 += 1

		if i1 == len(arr_1):
			ans_arr += arr_2[i2:]
		else:
			ans_arr += arr_1[i1:]
		return ans_arr

	def merge_sort(array):

		len_a = len(array)

		if len_a == 1:
			return array 
		elif len_a == 2:
			if array[1] < array[0]:
				array = [array[1], array[0]]
			return array 

		half_n = math.floor(len_a / 2)

		return merge(merge_sort(array[:half_n]), merge_sort(array[half_n:]))

	_start = time.time()
	array = merge_sort(array)
	_end = time.time()

	with open(f"./result/py.txt", "a") as f:
		f.write(f"merge_sort, {direc}, {_end - _start}\n")