#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

def arrayCheck(source, check):

  len_check = len(check)
  len_source = len(source)

  if (len_check == 0) or (len_source == 0) :
    print("One of the parameters was empty!")   
    return False

  if (len_check > len_source):
    print("Sublist was longer than the checklist!")   
    return False
    
  #Loop through the checklist, slicing it into sublists the size of the check list
  print("Checking " + str(source) + " for " + str(check))   
  for i in range(len_source + 1 - len_check):
    #get each slice
    if source[i:i+len_check] == check:
      return True

  return False


sub_list = []
print(arrayCheck([1, 1, 2, 3, 1], sub_list))       # Should trigger error: empty parameter

sub_list = [1, 2, 3]
print(arrayCheck([1, 1], sub_list))                # Should trigger error: check list is longer than source!
print(arrayCheck([1, 1, 2, 3, 1], sub_list))       # True
print(arrayCheck([1, 1, 2, 4, 1], sub_list))       # False 
print(arrayCheck([1, 1, 2, 1, 2, 3], sub_list))    # True

sub_list = [4]
print(arrayCheck([1, 1, 2, 3, 1], sub_list))       # False
print(arrayCheck([1, 1, 2, 4, 1], sub_list))       # True 
print(arrayCheck([4, 1, 2, 1, 2, 3], sub_list))    # True


#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(str):
  return str[::2]

print(stringBits('Hello')) 
print(stringBits('Hi')) 
print(stringBits('Heeololeo')) 


#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(a, b):

  if (len(a) == 0) or (len(b) == 0) :
    print("One of the parameters was empty!")   
    return False

  if (len(a) > len(b)):
    long_string = a.lower()
    short_string = b.lower()
  else:
    long_string = b.lower()
    short_string = a.lower()

  return (long_string[len(long_string) - len(short_string):] == short_string)

print(end_other('Hiabc', 'abc'))      # True
print(end_other('AbC', 'HiaBc'))      # True
print(end_other('abc', 'abXabc'))     # True
print(end_other('Ab', 'HiaBc'))       # False

#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(str):
  return "".join([2*c for c in str])

print(doubleChar('The'))       # 'TThhee'
print(doubleChar('AAbb'))      # 'AAAAbbbb'
print(doubleChar('Hi-There'))  # 'HHii--TThheerree'


#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
def fix_teen(n):
  #Are they a teen?, and are they an exception?
  if ((n > 12) and (n < 20)) and ((n != 15) and (n != 16)):
    return 0
  return n

print(no_teen_sum(1, 2, 3))     # 6
print(no_teen_sum(2, 13, 1))    # 3
print(no_teen_sum(2, 1, 14))    # 3
print(no_teen_sum(2, 13, 15))   # 17



#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
  return len([n for n in nums if (n%2 == 0)])

print(count_evens([2, 1, 2, 3, 4]))    # → 3
print(count_evens([2, 2, 0]))          # → 3
print(count_evens([1, 3, 5]))          # → 0
