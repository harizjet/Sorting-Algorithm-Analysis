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
	const pivot = function (array, st, ed) {
		let piv_i = Math.floor((ed-st)/2)+st;
		let piv = array[piv_i];
		let il = st, ir = ed;

		while (il < ir) {
			while ((array[il] <= piv || il == piv_i) && il < ed) {
				il ++;
			}

			while ((array[ir] >= piv || ir == piv_i) && ir > st) {
				ir --;
			}

			if (il < ir) {
				[ array[il], array[ir] ] = [ array[ir], array[il] ];
			}
		}
		if (piv_i > ir && piv_i < il) {
			return piv_i;
		} else if (piv_i <= ir) {
			[ array[piv_i], array[ir] ] = [ array[ir], array[piv_i] ];
			return ir;
		} else {
			[ array[piv_i], array[il] ] = [ array[il], array[piv_i] ];
			return il;
		}
	}

	const quicksort = function (array, st, ed) {
		if (st < ed) {
			let i = pivot(array, st, ed);

			quicksort(array, st, i-1);
			quicksort(array, i+1, ed);
		} 
	}

	_start = process.hrtime();
	quicksort(array, 0, array.length-1);
	_end = process.hrtime();
}

main();

fs.writeFileSync("./result/js.txt", `quick_sort, ${direc}, ${(_end[0] + _end[1]/1000000000) - (_start[0] + _start[1]/1000000000)}\n`, {encoding: 'utf8', flag:'a'});