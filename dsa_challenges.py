#Function 1: Filter even numbers and sort them
def filter_and_sort_even_numbers(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    evens.sort()
    return evens
# Function 2: Count characters frequency (case-insensitive)
def count_character_frequency(text):
    frequency = {}
    for char in text.lower():
        if char.isalpha():  # Count only alphabetic characters
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency

#test calls

print(filter_and_sort_even_numbers([3,1,4,7,1,5,9,2,6,8]))
print(count_character_frequency("This my task for basic Data Structure and Algorithm"))
