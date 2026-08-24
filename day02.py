# === CONDITIONALS ===

def even_or_odd(number):
    # Fixed: Return the string instead of printing it
    if number % 2 == 0:
        return "even"
    return "odd"  # Simplified: "else" is redundant after a return

print(even_or_odd(7))
print(even_or_odd(4))


def number_type(number):
    if number < 0:
        return "negative"
    if number == 0:
        return "zero"
    return "positive"

print(number_type(1))
print(number_type(-2))


def get_grade(grade):
    # Simplified: Sequential execution eliminates the need for 'and'
    if grade < 60:
        return "F"
    if grade < 70:
        return "D"
    if grade < 80:
        return "C"
    if grade < 90:
        return "B"
    if grade <= 100:
        return "A"
    return "Invalid grade"  # Handles numbers over 100

print(get_grade(89))
print(get_grade(59))


# === LOOPS ===

def sum_num(numbers):
    total = 0  # Fixed: Avoid shadowing the built-in 'sum' function
    for num in numbers:
        total += num  # Optimized: Used the += xsoperator
    return total

print(sum_num([2, 3, 4]))

def count_evens(numbers):
    evens = 0
    for num in numbers:
        if num % 2 == 0:
            evens += 1
    return evens

print(count_evens([1,2,4,7,8,10]))

def find_largest(numbers):
    if not numbers:
        return 'No numbers'
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(find_largest([4,2,9,1,7]))

## While loop

count = 0
while count < 5:
    print(count)
    count += 1

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    return number

print(fizzbuzz(3)) # "Fizz"
print(fizzbuzz(5)) # "Buzz"
print(fizzbuzz(15)) # "FizzBuzz"
print(fizzbuzz(7)) # 7

def second_largest(numbers):
    if len(set(numbers)) < 2:
        return None
    largest = float('-inf')
    sub_largest = float('-inf')

    for num in numbers:
        if num > largest:
            sub_largest = largest 
            largest = num
        elif num > sub_largest and num != largest:
            sub_largest = num
    return sub_largest

print(second_largest([10,5,8,29,15]))