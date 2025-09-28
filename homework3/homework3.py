# File: Homework 3

# --- Print Functions ---

# 3.1
def say_goodbye(name):
    print("Goodbye,", name)
say_goodbye("Sophie")

# 3.2 
def area_of_circle(Radius):
    Area = 3.14 * Radius ** 2
    print(Area)
area_of_circle(4)


# --- Return Functions ---

# 4.1
def subtract(a, b):
    return(a - b)
print(subtract(6, 2))

def multiply(a, b):
    return(a * b)
print(multiply(6, 2))

def divide(a, b):
    return (a / b)
print(divide(6, 2))

# --- Conditionals --- 

# 5.1
def min_max_daily_temp(daily_temperatures):
    return(min(daily_temperatures), max(daily_temperatures))
print(min_max_daily_temp([75, 79, 86, 80, 74, 91, 82]))

# 5.2
def is_weekend(day):
    if 5 < day <= 7:
        return True
    else: 
        return False
print(is_weekend(4))

# 5.3
def fuel_efficiency(miles, gallons):
    return((miles / gallons, "miles per gallon"))
print(fuel_efficiency(70, 3))

# 5.4
def encode(n):
    final_digit = n % 10
    remove_final_digit = n // 10
    return(remove_final_digit + final_digit * (10 ** len(str((remove_final_digit)))))

print(encode(12345))
    

# --- Loops ---

# 6.1 
def power(number, exponent):
    result = 1
    if exponent >= 0:
        for i in range (exponent):
            result = result * number
    else:
        for i in range (abs(exponent)):
            result = result / number      
    return result
print(power(4, -1))

# 6.2.1
def maximum_for(list):
    max = list[0]
    for i in range (len(list)):
        if max < list[i]:
            max = list[i]
    return max
my_list = [-45, 2, 0.456, 3, 102, 43]
print(maximum_for(my_list))

def minimum_for(list):
    min = list[0]
    for i in range (len(list)):
        if min > list[i]:
            min = list[i]
    return min
print(minimum_for(my_list))

# 6.2.2
def maximum_while(list):
    i = 0
    max = list[i]
    while i < len(list):
        if max < list [i]:
            max = list[i]
        i += 1
    return max
print(maximum_while(my_list))

def minimum_while(list):
    i = 0
    min = list[i]
    while i < len(list):
        if min > list [i]:
            min = list[i]
        i += 1
    return min
print(minimum_while(my_list))

# 6.3
def sum_of_digits(number):
    sum = 0
    while number > 0:
        digit_i = number // (10 ** (len(str(number))-1))
        number %= 10 ** (len(str(number))-1)
        sum += digit_i
    return sum
print(sum_of_digits(465))


# --- Running Your Script ---

#7.1
new_list = [3.2, 1, 76, 14]
print(maximum_for(new_list))
result = maximum_for(new_list) # maximum value of the list
print(f"The result of maximum_for (6.2.1) with new_list = {3.2, 1, 76, 14} is {list}.")
