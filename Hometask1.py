import numbers
import random
from operator import index

# Create a list of 100 random numbers ranging from 0 to 1000
random_numbers = [random.randint(0, 1000) for i in range(100)]
print("list of random numbers " + str(random_numbers))

# Create function to sort unsorted list
def sort (unsorted_list):
    # Create variable that is equal to the length of list
    n = len(unsorted_list)
    # Create temporary list that is equal to initial list
    unsorted_temp = unsorted_list[:]
    # Create empty list for result
    sorted_list = []
    # Iterate through the list as many times as there are elements in unsorted_list.
    for i in range(n):
        # Initialize `index_min` to point to the first element of unsorted_list
        index_min = 0
        # Assume the first element of the unsorted list is the minimum
        min_value = unsorted_list[index_min]
        # Iterate over elements in `unsorted_temp`, starting from the second element to compare it with min_value
        for j in range (1, len(unsorted_temp)):
            # Validate if every element from unsorted_temp is less than min_value
            if unsorted_temp[j] < min_value:
                # If element from unsorted_temp is less than min_value, than  this element will become min_value
                min_value = unsorted_temp[j]
                # and index_min will be the index of min_value element in unsorted_temp
                index_min = j
        # Add min_value to sorted_list
        sorted_list.append(min_value)
        # Delete min_value from unsorted_temp, because not to compare numbers with it in subsequent iterations
        unsorted_temp.pop(index_min)
    # Return sorted list
    return sorted_list
# Create sorted list of random_numbers
sorted_numbers = sort(random_numbers)
print("list of sorted numbers " + str(sorted_numbers))

#Create function to check if number is even
def is_even(number):
    try:
        # Check if input is number
        isinstance(number, numbers.Number)
    except ValueError:
        # If it is not number, throw exception
        print("Please enter valid integers.")
    # Check, if number is even
    if number%2==0:
        return True
    else:
        return False

# Calculate average for even numbers
def average_even (some_list):
    # Initialize the sum of even numbers in the list.
    sum_numbers = 0
    # Initialize the count of even numbers found in the list.
    count_numbers = 0
    # Loop through each index from 0 to the length of some_list.
    for i in range(len(some_list)):
        # Check if the current element at index i is even using the is_even function.
        if is_even(some_list[i]):
            # Add the even number to sum_numbers.
            sum_numbers+=some_list[i]
            # Increment the count of even numbers found.
            count_numbers+=1
    # Check, if count_numbers is not equal to zero
    if count_numbers==0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    # Return the computed average calculated by dividing the sum of even numbers by their count.
    return sum_numbers/count_numbers

def average_odd (some_list):
    # Initialize the sum of odd numbers to zero.
    sum_numbers = 0
    # Initialize the count of odd numbers to zero.
    count_numbers = 0
    # Iterate over each index from 0 to the length of 'some_list'.
    for i in range(len(some_list)):
        # Check if the current element is odd using is_even function negated.
        if not is_even(some_list[i]):
            # If the element is odd, add it to 'sum_numbers'.
            sum_numbers+=some_list[i]
            # Increment the count of odd numbers.
            count_numbers+=1
    # Check, if count_numbers is not equal to zero
    if count_numbers == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    # Return the computed average calculated by dividing the sum of even numbers by their count.
    return sum_numbers / count_numbers

average_even_numbers = average_even(sorted_numbers)
average_odd_numbers = average_odd(sorted_numbers)
print("Average for even numbers is "+ str(average_even_numbers))
print("Average for odd numbers is "+ str(average_odd_numbers))

