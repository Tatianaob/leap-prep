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
        total += num  # Optimized: Used the += operator
    return total

print(sum_num([2, 3, 4]))
