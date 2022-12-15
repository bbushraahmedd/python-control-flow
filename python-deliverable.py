# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(alphabet[1])
# 2. Write the code that determines whether the letter entered is a vowel
letter = input('enter a letter: ')
if letter == 'a' or letter == 'e' or letter == 'i'or letter == 'o' or letter == 'u':
    print('its a vowel!')
# else:
#     print('not it')
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant
alphabet = input('enter a letter of the alphabet ').lower()
if alphabet in ["a","e","i","o","u"]:
    print(f'{alphabet} is a vowel')
else:
    print(f'{alphabet} is a consonant')
   
# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.
while True:
    phrase = input('please enter a word or phrase ').lower()
    if phrase == 'quit':
        break
    else:
        print(f'the user entered {len(phrase)} characters long')

# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer
human_years = int(input('Input a dogs age in human years: '))
if human_years <= 2:
    dog_years = human_years * 10
else:
    dog_years = 20 + (human_years-2)*7
print(f'The dogs age in dog years is {dog_years}')
   
# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
a = int(input('Enter the length of a: '))
b = int(input('Enter the length of b: '))
c = int(input('Enter the length of c: '))

if a == b and c == a:
    print('the triangle is equalateral - all three sides are equal in length')
elif a == b or b == c or c == a:
    print('the triangle is isoceles - two sides are the same length')
else:
    print('the traingle is scalene')

# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it
term = 0
a = 0
b = 1
while term < 51:
  if term < 2:
    print(f'term: {term} / number: {term}')
  else:
    num = a + b
    print(f'term: {term} / number: {num}')
    a = b
    b = num
  term += 1

# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.
month = input('enter month of the year (jan - dec): ')
day = input('enter day of month: ')

if month in ('jan', 'feb', 'mar'):
    season = 'winter' 
elif month in ('apr', 'may', 'jun'):
    season = 'spring' 
elif month in ('jul', 'aug', 'sep'):
    season = 'summer' 
else:
    season = 'fall'
if month == 'mar' and day > 19:
    season = 'spring'
elif month == 'jun' and day > 20:
    season = 'summer'
elif month == 'sep' and day > 21:
    season = 'fall'
elif month == 'dec' and day > 20:
    season = 'winter'
print(f'{month} {day} is in {season}')