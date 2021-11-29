// input dependencies
const prompt = require('readline-sync');
const fs = require('fs');

let direc = process.argv.slice(2)[0];
let txt = fs.readFileSync(`./data/${direc}.txt`).toString();

if (txt.length === 0) {
	txt = prompt.question();
}

let array = txt.split(',').map((a) => {
	return parseInt(a.trim(), 10);
});

function main() {

	// algo start
	const merge = function (arr1, arr2) {
		let ans_arr = [];
		let ir = 0, il = 0;

		while (ir < arr1.length && il < arr2.length) {
			if (arr1[ir] < arr2[il]) {
				ans_arr.push(arr1[ir]);
				ir ++;
			} else {
				ans_arr.push(arr2[il]);
				il ++;
			}
		}

		if (arr1.length == ir) {
			ans_arr = ans_arr.concat(arr2.slice(il));
		} else {
			ans_arr = ans_arr.concat(arr1.slice(ir));
		}
		return ans_arr;
	}

	const mergesort = function (arr) {
		let len_arr = arr.length;

		if (len_arr == 1) {
			return arr;
		} else if (len_arr == 2) {
			if (arr[0] > arr[1]) {
				arr = Array(arr[1], arr[0]);
			}
			return arr;
		} else {
			let half_arr = Math.floor(len_arr / 2);

			return merge(mergesort(arr.slice(0, half_arr)), mergesort(arr.slice(half_arr)));
		}
	}

	_start = process.hrtime();
	array = mergesort(array);
	_end = process.hrtime();
}

main();

fs.writeFileSync("./result/js.txt", `merge_sort, ${direc}, ${(_end[0] + _end[1]/1000000000) - (_start[0] + _start[1]/1000000000)}\n`, {encoding: 'utf8', flag:'a'});