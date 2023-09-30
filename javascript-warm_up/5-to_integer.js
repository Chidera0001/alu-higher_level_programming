#!/usr/bin/node
const myFunction = process.argv;
const conV = Number(myFunction[2]);
if (conV) {
  console.log(`My number: ${myFunction[2]}`);
} else {
  console.log('Not a number');
}