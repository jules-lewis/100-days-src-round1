/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!


///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop

// While Loop
var iWhile = 1
while(iWhile <= 5){
    console.log("Hello " + iWhile);
    iWhile++;
}

// For Loop
for (let iFor = 1; iFor <= 5; iFor++){
    console.log("Hello " + iFor);
}


///////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// While Loop
var iWhile = 1
var numbers = ""
while(iWhile <= 26){
    numbers += iWhile + " ";
    iWhile += 2;
}
console.log(numbers);

// For Loop
var numbers = ""
for (let iFor = 1; iFor <= 26; iFor +=2){
    numbers += iFor + " ";
}
console.log(numbers);