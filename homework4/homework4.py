# File: Homework4.py


# --- List Operations ---

fav_foods = ["strawberries", "pie", "pasta", "sushi", "pizza"]

print(fav_foods[1])

print(fav_foods[-1])

fav_foods.append("soup")

fav_foods.insert(0, "apple")

fav_foods.remove("pasta")

print(len(fav_foods))

for food in fav_foods:
    print(food.upper())

new_list = fav_foods[0::5]

if "potato" in fav_foods:
    print("A potato!")
else:
    print("No potato!")

# --- Slicing and Striding ---

numbers = list(range(21))
def get_first_15(my_list):
   return my_list[0:16]
print(get_first_15(numbers))

# I encountered this error:
#      line 34, in <module>
#         print(get_first_15(numbers))
#.     TypeError: 'list' object is not callable
# I origionally wrote:
#        numbers = list(range(21))
#        get_first_15 = numbers[0:16]
# I did not define get_first_15 as a function so I could not insert a variable into it.
# I fixed this by defining get_first_15 as a function and creating an intermediate variabe "my_list".

def get_every_5th(first):
     return get_first_15(first[::5])
print(get_every_5th(numbers))

def reverse_and_stride(first):
    reverse = get_every_5th(first[::-1])
    return reverse[::3]
print(reverse_and_stride(numbers))

# --- Nested Lists ---

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2])
numbers.append([10, 11, 12])

def sum_nested(my_list):
    sum_total = 0
    for i in my_list:
        sum_total += sum(i)
    return sum_total

print(sum_nested(numbers))

# I encountered this error:
#     SyntaxError: invalid syntax
# I wrote: 
# def sum_nested(my_list):
#     sum_total = 0
#     for i in my_list:
#         sum_total += sum(i)
#     return sum_total
# I restarted my python tap and  the error disappeared.

def make_square_list():
    # new_list = []
    row_i = list(range(1,6))
    return [[k for k in range(1 + 5 * i,6 + 5 * i)] for i in range(5)] 

print(make_square_list())

five_by_five = make_square_list()

def change_3s(my_list):
    for i in range(len(my_list)):
        for k in range(len(my_list)):
            if my_list[i][k] % 3 == 0:
                my_list[i][k] = "?"
    return my_list

question_marks = change_3s(five_by_five)

# I encountered this error:
#     TypeError: not all arguments converted during string formatting
# I wrote: 
#   print(change_3s(five_by_five))
#   question_marks = change_3s(five_by_five)
# This confused VS Code because I called change_3s multiple times in a row.
# I fixed it by writing: 
#   uestion_marks = change_3s(five_by_five)

print(question_marks)

def sum_list(new_list):
    my_sum = 0
    for i in range(len(new_list)):
        for k in range(i):
            if new_list[i][k] != "?":
                my_sum += new_list[i][k]
    return my_sum

print(sum_list(question_marks))

# --- Dictionaries ---

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]
print(ages)
for name in ages:
    print(name, ages[name])

# Favorite function

print(make_square_list())
