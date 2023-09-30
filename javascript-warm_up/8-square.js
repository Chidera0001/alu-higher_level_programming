#!/usr/bin/node
let output;
const myFunction = process.argv;
const conV = Number(myFunction[2]);
if (conV) {
  for (let i = 0; i < conV; i++) {
    output = '';
    for (let j = 0; j < conV; j++) {
      output += 'X';
    }
    console.log(output);
  }
} else {
  console.log('Missing size');
}