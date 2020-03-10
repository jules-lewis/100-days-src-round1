var boolSpyName = false
var boolSpyAge = false
var boolSpyHeight = false
var boolSpyPet = false


var name = prompt("Please enter your name:").trim();
if (name.length > 0) {
    names = name.split(" ");
    if (names.length === 2) {
        if (names[0][0] === names[1][0]) {
            boolSpyName = true;
            console.log("Spy name checks out...");
        }
    }
}

var age = prompt("Please enter your age:");
if (!isNaN(age)) {
    if ((age >= 20) && (age <= 30)) {
        boolSpyAge = true;
        console.log("Spy age checks out...");
    }
}

var height = prompt("Please enter your height (cm):");
if (!isNaN(height)) {
    if (height >= 170) {
        boolSpyHeight = true;
        console.log("Spy height checks out...");
    }
}

var petName = prompt("What is the name of your favourite pet?");
if (petName.length > 0) {
    if (petName[petName.length-1].toLowerCase() === "y") {
        boolSpyPet = true
        console.log("Spy pet name checks out...");
    }
}

if (boolSpyName && boolSpyAge && boolSpyHeight && boolSpyPet) {
    console.log("Welcome friend.... here are the secret codes!");
}

alert("Thanks!")