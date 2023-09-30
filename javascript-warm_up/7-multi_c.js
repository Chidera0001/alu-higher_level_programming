#!/usr/bin/node
const myFunction = process.argv;
const youFunction = Number(myFunction[2]);
if (youFunction) {
  for (let i = 0; i < youFunction; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}