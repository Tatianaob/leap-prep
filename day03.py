# FUNCTIONS

def count_positive(numbers):
    positives = 0
    for num in numbers:
        if num > 0:
            positives += 1
    return positives

print(count_positive([3,-1,5,-2,0]))

def calculate_average(numbers):
    # average = total / number of values
    average = sum(numbers) / len(numbers)
    return int(average)
print(calculate_average([10,20,30]))


def find_smallest(numbers):
    if not numbers:
        return "No numbers"
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest
print(find_smallest([8, 3, 10, 2, 7]))




