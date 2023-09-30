#!/usr/bin/node
const myFunction = process.argv;
if (myFunction.length === 3) {
  console.log('Argument found');
} else if (myFunction.length > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}