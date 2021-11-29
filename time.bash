#!/bin/bash

if [[ $(wc -m result/py.txt) != "0" || $(wc -m result/js.txt) != "0" ]]; then

	read -p "Are you sure? " -n 1 -r 

	if [[ $REPLY =~ ^[Yy]$ ]]; then
		:
	else
		exit
	fi

fi

cat /dev/null > result/py.txt
cat /dev/null> result/js.txt

for filename in data/*.txt; do
	name=${filename##*/}
	base=${name%.txt}

	if [ $((base % 2500)) == "0" ]; then

		python ./py/merge_sort.py $base
		python ./py/radix_sort.py $base
		python ./py/quick_sort.py $base
		python ./py/insertion_sort.py $base
		python ./py/bubble_sort.py $base
		python ./py/selection_sort.py $base

		node ./js/merge_sort.js $base
		node ./js/radix_sort.js $base
		node ./js/quick_sort.js $base
		node ./js/insertion_sort.js $base
		node ./js/bubble_sort.js $base
		node ./js/selection_sort.js $base
	fi
done



