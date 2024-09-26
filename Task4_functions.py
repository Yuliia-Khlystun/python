import random
import string


def generate_random_keys():
    """Generates a set of random lowercase alphabet keys."""
    num_keys = random.randint(1, 26)  # 1 to 26 keys
    return random.sample(string.ascii_lowercase, num_keys)
def create_dictionary():
    """Creates a dictionary with random keys and random integer values between 0 and 100."""
    keys = generate_random_keys()
    return {key: random.randint(0, 100) for key in keys}
def generate_list_of_dicts(a, b):
    """Generates a list of dictionaries with a random length between a and b."""
    if not isinstance(a, int) or a < 0 or not isinstance(b, int) or b < 0 or b < a:
        raise ValueError("Please enter valid non-negative integers where b >= a.")
    num_dicts = random.randint(a, b)
    return [create_dictionary() for _ in range(num_dicts)]
def aggregate_keys(dict_list):
    """Aggregates all unique keys from a list of dictionaries."""
    keys_of_common_dict = set()
    for dictionary in dict_list:
        keys_of_common_dict.update(dictionary.keys())
    return keys_of_common_dict
def create_common_dict(dict_list, keys_of_common_dict):
    """Creates a common dictionary aggregating maximal values of keys across input dictionaries."""
    common_dict = {}
    for key in keys_of_common_dict:
        index_of_name_of_key = 0
        max_value_of_key = 0
        count_exist = 0
        for index, dictionary in enumerate(dict_list):
            if key in dictionary:
                count_exist += 1
                value_of_key = dictionary[key]
                if value_of_key > max_value_of_key:
                    max_value_of_key = value_of_key
                    index_of_name_of_key = index + 1
        if count_exist == 1:
            common_dict[key] = max_value_of_key
        else:
            name_of_key = key + "_" + str(index_of_name_of_key)
            common_dict[name_of_key] = max_value_of_key
    return common_dict
def main_function(a, b):
    dict_list = generate_list_of_dicts(a, b)
    print("List of dictionaries:")
    for i in dict_list:
        print(i)
    keys_of_common_dict = aggregate_keys(dict_list)
    dict_tuple = tuple(dict_list)
    common_dict = create_common_dict(dict_tuple, keys_of_common_dict)
    print("common dict", common_dict)
main_function(2,10)