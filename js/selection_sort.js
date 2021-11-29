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
	let len_arr = array.length;

	_start = process.hrtime();
	// algo start
	for (let i = 0; i < len_arr - 1; i ++) {
		for (let ir = i+1; ir < len_arr; ir ++) {
			if (array[ir] < array[i]) {
				[ array[ir], array[i] ] = [ array[i], array[ir] ];
			}
		}
	}
	_end = process.hrtime();
}

main();

fs.writeFileSync("./result/js.txt", `selection_sort, ${direc}, ${(_end[0] + _end[1]/1000000000) - (_start[0] + _start[1]/1000000000)}\n`, {encoding: 'utf8', flag:'a'});