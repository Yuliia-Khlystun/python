import random
import string


def create_a_list_of_dicts (a, b):
    # Check if inputs are numbers
    if not isinstance(a, int) or a<0 or not isinstance(b, int) or b<0 or b<a:
        raise ValueError("Please enter valid integers.")
    # Determine a random number of dictionaries to create (between a and b)
    num_dicts = random.randint(a, b)
    # Create empty list of dicts
    list_of_dicts = []
    # Loop to generate each dictionary to be added to the list
    for k in range(num_dicts):
        # Create an empty dictionary
        dictionary = {}
        # Determine a random number of keys (letters) for each dictionary
        num_keys = random.randint(1, 26)  # Assuming 1 to 26 keys per dictionary, as we have 26 letters in alphabet
        # Generate a random set of letters to use as keys
        keys = random.sample(string.ascii_lowercase, num_keys)
        for key in keys:
            # Assign each key a random value between 0 and 100
            dictionary[key] = random.randint(0, 100)
        # Add the created dictionary to the list of dictionaries
        list_of_dicts.append(dictionary)
    # Return the list of crated dictionaries
    return list_of_dicts

# Create a new list of dictionaries with a random number of dictionaries between 2 and 10
new_list_of_dicts = create_a_list_of_dicts(2, 10)
# Print a title message indicating that the following output will be a list of dictionaries
print("List of dictionaries")
# Iterate through each dictionary in the newly created list of dictionaries
for i in new_list_of_dicts:
    # Print each dictionary found in the list
    print(i)
# Create one common dict for previously generated list of dicts
def create_common_dict(dict_list):
    # Initialize an empty dictionary to store the aggregated results
    common_dict = {}
    # Create an empty set to store unique keys found across all dictionaries
    keys_of_common_dict = set()
    # Iterate through each dictionary in the list
    for dictionary in dict_list:
        # Retrieve keys from the current dictionary
        keys_of_dict = dictionary.keys()
        # Update the set of unique keys with new keys found in this dictionary
        keys_of_common_dict.update(keys_of_dict)
    # Print the set of all unique keys accumulated from all dictionaries
    print("keys_of_common_dict ", keys_of_common_dict)
    # Iterate through each unique key to perform aggregation
    dict_tuple=tuple(dict_list)
    for key in keys_of_common_dict:
        # Initialize variables for tracking the index of the dictionary and the maximum value associated with the key
        index_of_name_of_key = 0
        max_value_of_key = 0
        # Counter to track the current dictionary index
        count_all = 1
        # Counter to track how many dictionaries contain the current key
        count_exist=0
        # Iterate through each dictionary again to find the maximum value for the current key
        for dictionary in dict_tuple:
            # Check if the current key exists in the dictionary
            if dictionary.get(key) is not None:
                # Fetch the value associated with the key
                value_of_key = dictionary.get(key)
                # Increment counter for dictionaries containing the key
                count_exist+=1
                # Update maximum value and its index if this value is greater than the current maximum
                if value_of_key>max_value_of_key:
                    max_value_of_key=value_of_key
                    index_of_name_of_key = count_all
            # Increment the dictionary index counter
            count_all += 1
            # If the key exists in only one dictionary, use the original key name in the common_dict
        if count_exist==1:
            common_dict[key]=max_value_of_key
        # If the key exists in multiple dictionaries, append the index of its maximum occurrence
        else:
            name_of_key = key + "_" + str(index_of_name_of_key)
            common_dict[name_of_key]=max_value_of_key
    # Return the aggregated dictionary containing maximum values (and indexed keys if necessary)
    return  common_dict

# Create the common aggregated dictionary from a list of dictionaries
common_dict=create_common_dict(new_list_of_dicts)
# Print the resulting common dictionary for verification
print("common dict", common_dict)