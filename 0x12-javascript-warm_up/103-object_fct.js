#!/usr/bin/node
//  new function incr  increments an integer value

const myObject = 
	{
	type: 'object',
	value: 12
	};
	console.log(myObject);
	myObject.incr = function () {
	myObject.value++;
	};
	myObject.incr();
	console.log(myObject);
	myObject.incr();
	console.log(myObject);
	myObject.incr();
	console.log(myObject);
