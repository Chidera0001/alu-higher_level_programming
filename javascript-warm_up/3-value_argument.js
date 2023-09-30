#!/usr/bin/node
const myFunction = process.argv;
if (myFunction[2] != null) {
  console.log(myFunction[2]);
} else {
  console.log('No argument');
}