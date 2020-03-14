
document.getElementById("btn-reset").addEventListener("click", function() {
    cells = document.querySelectorAll(".cell");
    for (let index = 0; index < cells.length; index++) {
        cells[index].textContent = "";
        
    }
})

cells = document.querySelectorAll(".cell");
for (let index = 0; index < cells.length; index++) {
    cells[index].addEventListener("click", cellClick);
}

function cellClick() {

    if (this.textContent === "") {
        this.textContent = "X";
    } else if (this.textContent === "X") {
        this.textContent = "O";
    } else {
        this.textContent = "";
    }
    
}