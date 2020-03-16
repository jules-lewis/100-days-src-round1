
//Colours used in the game
var player1Color = 'rgb(86, 151, 255)';    //Blue
var player2Color = 'rgb(237, 45, 73)';     //Red
var colorGrey = 'rgb(128, 128, 128)';      //Grey

//Turn this off when someone wins
var game_on = true;

//Store the board as a list of rows
var board = $('table tr');

// Start with Player One
var currentPlayer = 1;
var currentName = player1;
var currentColor = player1Color;

// Start with Player One
var player1 = prompt("Player One: Please enter your name, you will be BLUE");
var player2 = prompt("Player Two: Please enter your name, you will be RED");
$('#prompt').text(player1+": it is your turn, please pick a column to drop your blue chip.").css('color', currentColor);

// The main game logic - respond to button clicks if the game is still running
$('.board button').on('click',function() {

  if (game_on) {

    // Recognize what column was chosen
    var col = $(this).closest("td").index();
  
    // Get back bottom available row to change
    var bottomAvail = checkBottom(col);

    //We only respond to the click if there's actually somewhere to put the piece
    if (bottomAvail !== -1) {

      // Drop the chip in that column at the bottomAvail Row
      changeColor(bottomAvail,col,currentColor);
  
      // Check for a win or a tie.
      if (horizontalWinCheck() || verticalWinCheck() || diagonalWinCheck()) {
        //If there's a winner, end the game  
        gameEnd(currentName, currentColor);
      } else {
        //Otherwise get ready for the next go
        //Set variables according to whose turn it is
        if (currentPlayer === 2) {
          currentPlayer = 1;
          currentName = player1;
          currentColor = player1Color;
          $('#prompt').text(currentName+": it is your turn, please pick a column to drop your blue chip.").css('color', currentColor);
        } else {
          currentPlayer = 2;
          currentName = player2
          currentColor = player2Color;
          $('#prompt').text(currentName+": it is your turn, please pick a column to drop your red chip.").css('color', currentColor);
        }
      }
    }
  }    
})
  

//////////////////////////////////////////////////////////////
//
// HELPER FUNCTIONS
//
//
  
// Change the color of the button at rowIndex, colIndex to color
function changeColor(rowIndex,colIndex,color) {
    return board.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color',color);
}
  
// Return the color of the button at rowIndex, colIndex
function checkColor(rowIndex,colIndex) {
    return board.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}

// Returns the lowest row that is still grey in column colIndex
function checkBottom(colIndex) {
  var colorReport = checkColor(5,colIndex);
  for (var row = 5; row > -1; row--) {
    colorReport = checkColor(row,colIndex);
    if (colorReport === colorGrey) {
      return row
    }
  }
  //If there are no grey buttons, ignore the click
  return -1
}
  
// Check to see if 4 inputs are the same color
function colorMatchCheck(one,two,three,four){
  return (one===two && one===three && one===four && one !== colorGrey && one !== undefined);
}
  
// Check for Horizontal Wins
function horizontalWinCheck() {
  for (var row = 0; row < 6; row++) {
    for (var col = 0; col < 4; col++) {
      if (colorMatchCheck(checkColor(row,col), checkColor(row,col+1) ,checkColor(row,col+2), checkColor(row,col+3))) {
        console.log('Horizontal match!');
        reportWin(row,col);
        return true;
      }else {
        continue;
      }
    }
  }
}
  
// Check for Vertical Wins
function verticalWinCheck() {
  for (var col = 0; col < 7; col++) {
    for (var row = 0; row < 3; row++) {
      if (colorMatchCheck(checkColor(row,col), checkColor(row+1,col) ,checkColor(row+2,col), checkColor(row+3,col))) {
        console.log('Vertical match!');
        reportWin(row,col);
        return true;
      }else {
        continue;
      }
    }
  }
}
  
// Check for Diagonal Wins
function diagonalWinCheck() {
  for (var col = 0; col < 5; col++) {
    for (var row = 0; row < 7; row++) {
      if (colorMatchCheck(checkColor(row,col), checkColor(row+1,col+1) ,checkColor(row+2,col+2), checkColor(row+3,col+3))) {
        console.log('Diagonal Match - Down and to the right');
        reportWin(row,col);
        return true;
      }else if (colorMatchCheck(checkColor(row,col), checkColor(row-1,col+1) ,checkColor(row-2,col+2), checkColor(row-3,col+3))) {
        console.log('Diagonal Match - Up and to the right');
        reportWin(row,col);
        return true;
      }else {
        continue;
      }
    }
  }
}
  
// Game End
function gameEnd(winningPlayer, winnerColor) {
  $('.slide-up').slideUp("slow");
  $('#prompt').text(winningPlayer+" has won! Refresh your browser to play again!").css('color', winnerColor)
  game_on = false
}
  
// Report to the console where the winning piece was placed
function reportWin(rowNum,colNum) {
    console.log("You won starting at row " + rowNum + ", column " + colNum + ".");
}

