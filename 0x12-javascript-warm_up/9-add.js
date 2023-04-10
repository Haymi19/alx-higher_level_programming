#!/usr/bin/node

// Script that prints the addition of 2 integers.

function add(a, b) {
	let add = a + b;
	return add;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
