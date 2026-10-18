#Function 1: calculate Average safely
def calculate_average_safely(numbers):
    try:
        total = 0
        for i in range (len(numbers)):
            total += numbers[i]

        return total / len(numbers)
    except ZeroDivisionError:
        print("Error: Cannot calculate average of an empty list.")
        return None

#function 2: safe list element access
def get_list_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print(f"Error: Index {index} is out of bounds for the list.")
        return None
    except TypeError:
        print("Error: Provided object is not a list.")
        return None

# --Test Data for Debugging--
data1 = [10,20,30,40,50]
data2 = [5,15]
data3 = []
print(f"Average of data1: {calculate_average_safely(data1)}")
print(f"Average of data2: {calculate_average_safely(data2)}")
print(f"Average of data3: {calculate_average_safely(data3)}")

#-- Test cases for Error Handling--

print("\n testing get_list_element:")

#valid case

print(get_list_element([1,2,3],1))

#out of bounds

print(get_list_element([1,2,3],10))

#wrong type

print(get_list_element("not a list",0))