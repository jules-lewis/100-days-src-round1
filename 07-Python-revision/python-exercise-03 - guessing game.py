'''
Python revision: Guessing Game
'''

'''
This is a basic recreation of the Mastermind game, 
where the computer sets a puzzle for the player. The 
computer will pick a four digit number using the digits 
1-6.

The player will then have up to (MAX_TURNS) guesses to 
work out the number. After each guess, the player will 
be told how many digits they guessed correctly and in 
the correct place, and how many numbers they guessed 
correctly, but in the *wrong* place.

For example, if the computer sets "3512" and the 
player guesses "4526" they will be told they  got one 
digit completely right (the '5'), and one correct 
but in the wrong place (the '2'). The player is not
told *which*  digits they got correct, but they do get 
to see all their previous guesses.
'''

##########################################
##
## Imports
import random

##########################################
##
## Variables, and pick some numbers for the computer
previous_guesses = []
play_game = True
count_turns = 0
MAX_TURNS = 10

##########################################
##
## Functions

def generate_puzzle():
  '''
  Generates a list containing four numbers from 1 to 6
  Input:  --
  Return: List containing four integers, from 1 to 6 (can be repeated)
  '''
  
  new_puzzle = []
  for i in range(4):
    new_puzzle.append(random.randint(1,6))
  return new_puzzle

def check_guess(the_code, player_guess):
  '''
  Checks the player's guess against the computer's code
  Input:  The computer's code, as a list of four integers
          The player's guess, as a four digit string (which
          will already have been checked)
  Return: List containing two numbers:
          - the number of completely correct guesses (correct
            digit, correct location)
          - the number of partially complete guesses (correct
            digit, wrong location)
  '''
  #Make a copy of the computer code, because we're going to edit
  #it a bit
  code_copy = the_code.copy()
  guess_copy = [int(c) for c in player_guess]
  
  #Our counters
  completely_correct = partially_correct = 0

  #check for completely correct guesses
  for i in range(4):
    if (guess_copy[i] == code_copy[i]):
      completely_correct += 1
      #make sure we don't accidentally count this again later
      code_copy[i] = 0

  #check for partially correct guesses
  for i in range(4):
    #check we haven't already matched this digit
    if (guess_copy[i] != 0):
      #is the digit somewhere else in the list?
      if (guess_copy[i] in code_copy):
        partially_correct += 1 
        #make sure we don't accidentally count this again later
        code_copy[code_copy.index(guess_copy[i])] = 0     

  return [completely_correct, partially_correct]  

def get_player_guess():
  '''
  Gets some input from the user. Checks to ensure the user
  has entered exactly four digits, using only the digits 1-6
  Input:  n/a
  Return: the user input, in correct format
  '''
  check_format = False
  while not check_format:
    print("-----------------------------------------------------")
    user_input = input("Guess! Please enter a four digit guess, using only the digits 1-6. > ")
    if (len(user_input) == 4):
      if (user_input.isnumeric()):
        as_number = int(user_input)
        if (1110 < as_number < 6667):
          return user_input
    print("Sorry, your input was not in the correct format.")


##########################################
##
## The game! Let's do some set-up
the_puzzle = generate_puzzle()

print("-----------------------------------------------------")
print("#####################################################")
print("#                                                   #")
print("#   W E L C O M E   T O   M A S T E R M I N D ! !   #")
print("#                                                   #")
print("#  The aim of the game is to guess a four digit     #")
print("#  code that I will generate. I will uses the       #")
print("#  digits 1 to 6, and I might repeat. For example,  #")
print("#  '1166', '4321', '1111', and '4545' are all       #")
print("#  valid codes.                                     #")
print("#                                                   #")
print("#  After each guess, I will tell you how many       #")
print("#  numbers you guessed correctly and in the         #")
print("#  correct place. I will also tell you if you got   #")
print("#  any correct numbers that are not in the right    #")
print("#  place.                                           #")
print("#                                                   #")
print("#  For example, if my code is '3512' and you guess  #")
print("#  '4526', I'll tell you one digit is completely    #")
print("#  correct (the '5'), and one is partially correct  #")
print("#  (the '2'). Obviously I won't tell you *which*    #")
print("#  digits you got right: that would be too easy!    #")
print("#  I will let you keep an eye on your previous      #")
print("#  guesses though, to save you writing them down.   #")
print("#  You will be allowed {} guesses.                  #".format(MAX_TURNS))
print("#                                                   #")
print("#              L E T ' S   P L A Y   ! !            #")
print("#                                                   #")
print("#####################################################")

#print(the_puzzle)   <--- uncomment this line if you want to see the code while debugging!

while play_game:

  str_guess = get_player_guess()
  guess_score = check_guess(the_puzzle, str_guess)
  count_turns += 1

  #Did they get it completely right?
  if (guess_score == [4, 0]):
    print("Well done! That took {} tries!".format(count_turns))
    play_game = False
  else:
    #Have they had all their turns?
    if (count_turns >= MAX_TURNS):
      print("-----------------------------------------------------")
      print("Sorry, you're out of tries! The code was '{}'. Better luck next time...".format("".join(the_puzzle)))
      print("-----------------------------------------------------")
      play_game = False
    else:
      previous_guesses.append([str_guess, guess_score])
      print("-----------------------------------------------------")
      print("You got {} in the right place, {} in the wrong place.".format(guess_score[0], guess_score[1]))
      print("-----------------------------------------------------")
      print("Your guesses so far:")
      for guess in previous_guesses:
        print("{}:  {} completely correct, {} partially correct".format(guess[0], guess[1][0], guess[1][1]))
      print("=====================================================")

