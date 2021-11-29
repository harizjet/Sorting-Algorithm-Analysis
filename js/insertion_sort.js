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
	for (let i = 1; i < len_arr; i++) {
		for (let il = i - 1; il >= 0; il--) {
			if (array[il+1] > array[il]) {
				break;
			}
			[ array[il], array[il+1] ] = [ array[il+1], array[il] ]
		}
	}
	_end = process.hrtime();
}

main();


fs.writeFileSync("./result/js.txt", `insertion_sort, ${direc}, ${(_end[0] + _end[1]/1000000000) - (_start[0] + _start[1]/1000000000)}\n`, {encoding: 'utf8', flag:'a'});