var students = []
var userEntry = ""


while (userEntry !== "quit") {
    
    userEntry = prompt("Enter a command (add, remove, display, quit):")

    //Treat pressing Cancel as though the user wanted to quit
    if (userEntry === null) { 
        userEntry = "quit" 
    } else {
        userEntry = userEntry.trim()
        userEntry = userEntry.toLowerCase()
        if (userEntry === "add") {
            addStudent();
        } else if (userEntry === "remove") {
            removeStudent();
        } else if (userEntry === "display") {
            console.log(students);
        } else if (userEntry === "quit") {
            alert("Goodbye! Refresh the page with F5 if you want to start again.")
        } else {
            alert("That is not a valid entry!");
        }
    }
}

function addStudent() {
    newUser = prompt("Enter the new student's name")
    if (newUser.length > 0) {
        newUser.trim()
        if (newUser.length > 0) {
            students.push(newUser)
        }
    }
}

function removeStudent() {
    if (students.length !== 0) {
        userToRemove = prompt("Enter the name of the student to remove")
        if (userToRemove.length > 0) {
            userToRemove.trim()
            if (userToRemove.length > 0) {
                var iFound = students.indexOf(userToRemove)
                if (iFound === -1) {
                    alert("Sorry, I couldn't find '" + userToRemove + "'.")
                } else {
                    students.splice(iFound, 1)
                }
            }
        }
    } else {
        alert("There are no students to remove!");
    }
}
    
