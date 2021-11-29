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
	const countsort = function (arr, exp) {
		let out = new Array(arr.length);
		let count = new Array(10);

		for (let i = 0; i < 10; i++) {
			count[i] = 0
		}
		for (let i = 0; i < arr.length; i++) {
			count[Math.floor(arr[i] / exp) % 10] ++;
		}
		for (let i = 1; i < 10; i++) {
			count[i] += count[i - 1];
		}
		for (let i = arr.length - 1; i >= 0; i--) {
			out[count[Math.floor(arr[i] / exp) % 10] - 1] = arr[i];
			count[Math.floor(arr[i] / exp) % 10]--;
		}
		for (let i = 0; i < arr.length; i++) {
			arr[i] = out[i];
		}
	}

	const radixsort = function (arr) {
		let m = Math.max(...arr);

		for (let exp = 1; Math.floor(m / exp) > 0; exp *= 10) {
			countsort(arr, exp);

		}
	}

	_start = process.hrtime();
	radixsort(array);
	_end = process.hrtime();
}

main();

fs.writeFileSync("./result/js.txt", `radix_sort, ${direc}, ${(_end[0] + _end[1]/1000000000) - (_start[0] + _start[1]/1000000000)}\n`, {encoding: 'utf8', flag:'a'});
