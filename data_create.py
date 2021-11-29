import numpy as np
import os

for d in range(1000, 50001):
	arr = np.random.choice(range(d), d, replace=False)
	file_n = '{}.txt'.format(d)
	if len(os.listdir('data/')) > 1:
		print("Data already exists")
		break
	file_l = os.getcwd() + '/data/' + file_n
	with open(file_l, 'w') as f:
		f.write(','.join([str(x) for x in arr]))