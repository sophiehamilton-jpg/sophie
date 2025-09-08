# File: homework1.py


# --- Variables and Data Types ---

a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals 
b = 1.5
print(b)
print(type(b)) # b is a float, a number with a decimal place
c = 3j
print(c)
print(type(c)) # c is a complex number, a function
d = "hello"
print(d)
print(type(d)) # d is a string, textual data
e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, a collection of numbers
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dict, a way to store data pairs
g = (1, 2)
print(g)
print(type(g)) # g is a tuple, a sequence of values
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, a collection of textual data
i = True
print(i)
print(type(i)) # i is a bool, a true/false statement
j = None
print(j)
print(type(j)) # j is a nonetype, an object that indicates no value
k = [True, "blue", 12]
print(k)
print(type(k)) # is a list
l = str(14)
print(l)
print(type(l)) # is a string, a sequence of characters
m = 1e4
print(m)
print(type(m)) # is a float, a number in scientific notation
# Questions
# 1. 9
# 2. integer, float, complex number, string, list, dict, tuple, bool, nonetype
# 3. e, h, and k; d and l; b and m
# 4. 1 is an integer. Adding str() makes the data type a string.
# 5. range
n = range(5)
print(n)
print(type(n)) # n is a range, a sequence of numbers


# --- Booleans ---

print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 is not equal to 9
print(10 <= 9) # False, 10 is not less than or equal to 9
print (bool("abc")) # True, any non-empty string evaluates to "true"
print(bool(123)) # True, any non-zero value evaluates to "true"
print(bool(["apple", "cherry", "banana"])) # True, the data set is non-empty
print(bool(True)) # True, the bool value "true" is true by definition
print(bool(False)) # False, the bool value "false" is false by definition
print(bool(0)) # False, a value of zero evaluates to "false"
print(bool("")) # False, an empty string evaluates to "false"
print(bool(" ")) # True, the space between the "" makes the statement non-empty
print(bool(())) # False, the tuple is empty
print(bool([])) # False, the list is empty
print(bool({})) # False, the dict is empty
print(bool(True and False)) # False, a boolean statement cannot be both True and False
print(bool(True and True)) # True, true is equivalent to true, which evaluates to true
print(bool(False and False)) # False, false = false, which evaluates to false
print(bool(True or False)) # True, at least one of the operands is true
print(bool(True or True)) # True, both of the operands are true
print(bool(False or False)) # False, neither operand is true
print(bool(not(False))) #True, the "not" command inverts the truth value
print(bool(not(True))) #False, the "not" command inverts the truth value
# Questions
# 1. All empty statements are False 
# 2. I was surprised that the presence of one True value renders an OR statement True
print(bool(1)) # 3. the value is non-zero
print(bool(3 < 2)) # 4. 3 is not less than 2


# --- Operators ---

# Arithmetic Operators
print(10 + 5) # 15, + performs addition
print(10 - 5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multiplication
print(6 / 3) # 2.0, / performs division
print(5 % 2) # 1, % divided 5 by 2 and outputted the remainder
print(3 ** 2) # 9, ** indicates an exponent
print(15 // 2) # 7, // divided 15 by two and outputted an integer approximation
# Comparison Operators
print(5 == 2) # False, == denotes equalness; 5 and 2 are not equal
print(10 != 10) # False, != denotes "not equal to"; 10 is equal to 10
print(2 < 5) # True, < indicates "less than"
print(12 > 5) # True, > indicates "greater than"
print(5 <= 6) # True, <= indicates "less than or equal to"
print(1 >= 10) # False, >= indicates "greater than or equal to"
# Assignments operators
x = 5
x += 5
print(x) # 10, the operator added 5 to the value of x
x -= 4
print(x) # 6, the operator subtracted 4 from the value of x
x *= 3 
print(x) # 18, the operator multiplied three by the value of x
# Logical operators
 # 1. The operator "and" returns "True" if all operands are true, and "False" if any operand is false
print(bool(x==18 and True))
print(bool(x==5 and True))
 # 2. The operator "or" returns "False" if all operands are false, and "True" if any are true
print(bool(3 > 1 or 0))
print(bool(3 < 1 or 0))
 # 3. The operator "not" inverts the truth of the operand
print(bool(not(1 >= 2)))
print(bool(not("abc")))
# More Questions
# 1. / performs division; // performs division but only outputs the integer part of the quotient
# 2. % divides and outputs the remainder; // outputs the integer after division
# 3. %: print(8 % 3)
# 4. Assignment operators assign a value to a variable


# --- Strings ---

my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0]) # Prints: h
print(my_string[1]) # Prints: e
print(my_string[2]) # Prints: l
print(my_string[3]) # Prints: l
print(my_string[4]) # Prints: o
print(my_string[-1]) # Prints: o
print(my_string[1:3]) # Prints: el
print(my_string[0:5:2]) # Prints: hlo
print(len(my_string)) # Prints: 5
print(my_string + "goodbye") # Prints: hellogoodbye
print(my_string * 7) # Prints: hellohellohellohellohellohellohello
# 1. Slicing is dividing a string into parts (manipulations 8 & 9)
name = "Oski"
print("Hello, my name is", name)
# 2. Prints: Hello, my name is Oski
name = "Oski"
print(f"Hello, my name is {name}")
# 3. Second statement is an f-string: a way to insert veriables into a string using {}


# --- Terminal Commands ---

# 1. cd
# Changes directories. Use it to move from one folder to another
# Example: cd python_decal_fa25

# 2. ls
# Lists directories: Use it to view a list directories within a folder
# Example: ls

# 3. ls -a 
# Lists all directories: Modifier to ls to ensure hidden directories are listed as well
# Example: ls -a

# 4. mkdir
# Make directory: creates a new directory
# Example: mkdir newfile

# 5. cat
# Concatenate: displays the contents of a file
# Example: cat homework1.py

# 6. pwd
# Print working directory: display current file path
# Example: pwd

# 7. cd ..
# Change directories to the parent directory
# Example: cd ..

# 8. cd .
# Change directories to the current directory
# Example: cd .

# 9. cd ~
# Return to root directory
# Example: cd ~

# 10. cp
# Copy: make a copy of a file or directory
# Example: cp python_decal_fa25

# 11. mv
# Moves a file to a new location
# Example: mv script.py /Users/sophiehamilton/

# 12. rm
# Remove: deletes a file or directory
# Example: rm script.py

# 13. clear
# Clears the terminal 
# Example: clear

# 14. grep
# Global regular expression print: searches for strings of text within files
# grep "print" python_decal_fa25

#Questions 
# 1. rmdir: deletes a directory. ex) rmdir sophie
# touch: creates a new file. ex) touch newfile
# nano: allows one to view and edit the contents of a file ex) nano datatypes.py
# 2. ls does not display the hidden files within a directory
# 3. hidden files begin with "."
# 4. 