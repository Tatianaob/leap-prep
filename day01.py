def greet(name):
    return f"Hello, {name}!"

print(greet("Tatiana"))


# It should return True if the number is even and False otherwise:
def is_even(number):
    if number % 2 == 0:
        return True
    return False

# I use the modulo operator to determine wheter dividing the number by two leaves
# a remainder. If the remainder is zero then the number is even.
# Time complexity O(1) because it performs a constant amount of work regardless of 
# how large the number is S
print(is_even(4))
print(is_even(7))


# Largest number
def find_largest(numbers):
    if len(numbers) == 0:
        return "No numbers"
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
        

print(find_largest([3,4,5,78,9]))
print(find_largest([-3,-2,-4]))

print(find_largest([]))

# Count character:
def count_character(text, character):
    characters = 0
    for char in text:
        if char == character:
            characters += 1
    return characters

print(count_character("banana", "a")) #returns 3

# reverse a string:
def reverse_string(text):
    # reversed_s = text[::-1]
    # return reversed_s
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

print(reverse_string("hello")) # olleh


# remove duplicates:

def remove_duplicates(numbers):
    duplicates = []
    for num in numbers:
        if num not in duplicates:
            duplicates.append(num)
            # numbers.remove(num)
    return duplicates



print(remove_duplicates([1,2,2,3,3,4])) # expected: [1,2,3,4]