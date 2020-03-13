// Part 6 - Objects Exercise


////////////////////
// OUTLINE
//
// Given the object:
//
// var employee = {
//   name: "John Smith",
//   job: "Programmer",
//   age: 31
// }

////////////////////
//
// PROBLEM 1 
//
// Add a method called nameLength that prints out the
// length of the employee's name to the console.

///////////////////
//
// PROBLEM 2
//
// Write program that will create an Alert in the browser of each of the
// object's values for the key value pairs. For example, it should alert:
//
// Name is John Smith, Job is Programmer, Age is 31.

///////////////////
//
// PROBLEM 3 
//
// Add a method called lastName that prints
// out the employee's last name to the console.
//
// You will need to figure out how to split a string to an array.
// Hint: http://www.w3schools.com/jsref/jsref_split.asp

var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  // Problem 1: begin
  nameLength: function() {
    return this.name.length;
  },
  // Problem 1: end
  // Problem 3: begin
  lastName: function() {
    var chunks = this.name.split(" ");
    return chunks[chunks.length-1];
  }
  // Problem 3: end
}

//Problem 1 Output
console.log("----------------------");
console.log("Problem 1");
console.log("----------------------");
console.log(employee.nameLength());
console.log("----------------------");


// Problem 2: begin
console.log("----------------------");
console.log("Problem 2");
console.log("----------------------");
for (const prop in employee) {
  if (typeof employee[prop] !== "function") {
    console.log(prop + " is " + employee[prop]);
  }
}
console.log("----------------------");
// Problem 2: end 

//Problem 3 Output
console.log("----------------------");
console.log("Problem 3");
console.log("----------------------");
console.log(employee.lastName());
console.log("----------------------");



