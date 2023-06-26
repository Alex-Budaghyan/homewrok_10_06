types_of_people = 10  # Assigns the value 10 to the variable 'types_of_people'
x = f"There are {types_of_people} types of people."  # Constructs a string with a variable using f-string
# formatting
binary = "binary"  # Assigns the string "binary" to the variable 'binary'
do_not = "don't"  # Assigns the string "don't" to the variable 'do_not'
y = f"Those who know {binary} and those who {do_not}."  # Constructs a string with multiple variables
# using f-string formatting
print(x)  # Prints the value of the variable 'x'
print(y)  # Prints the value of the variable 'y'
print(f"I said: {x}")  # Constructs a string with a variable using f-string formatting and prints it
print(f"I also said: '{y}'")  # Constructs a string with a variable using f-string formatting and prints it
hilarious = False  # Assigns the boolean value False to the variable 'hilarious'
joke_evaluation = "Isn't that joke so funny?! {}"  # Assigns a string with a placeholder to the variable
# 'joke_evaluation'
print(joke_evaluation.format(hilarious))  # Formats the variable 'hilarious' into the 'joke_evaluation'
# string and prints it
w = "This is the left side of..."  # Assigns the string "This is the left side of..." to the variable 'w'
e = "a string with a right side."  # Assigns the string "a string with a right side." to the variable 'e'
print(w + e)  # Concatenates the strings 'w' and 'e' using the + operator and prints the resulting string
