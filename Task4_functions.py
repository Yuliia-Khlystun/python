import random
import re
import string

from Classes import News, PrivateAd, RestaurantReview


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

def normalize_misspellings (text, old, new):
    # Normalize and correct misspellings in the text
    replaced_iz = text.lower().replace(old, new).capitalize()
    return replaced_iz

# Capitalize the first letter of each sentence:
def capitalize_first_letter(match):
    return match.group(0).upper()
def capitalize_text (text):
    capitalized_text = re.sub(r"(?<=[.!?])\s*(\w)", capitalize_first_letter, text)
    return capitalized_text

# Count all whitespace characters in the text
def count_whitespaces(text):
    whitespaces = re.findall(r'\s', text)
    count_whitespace = len(whitespaces)
    return count_whitespace

# Form a new sentence from the last word of each existing sentence
def add_sentence (text):
    last_words = re.findall(r'\b(\w+)\b(?=[.?!])', text)
    new_sentence = ' '.join(last_words) + '.'
    text += ' ' + new_sentence.capitalize()
    return text

def create_publication():
    kind_of_publication = input("Please, enter the type of publication: News, Private ad or Restaurant Review ")
    file_name = input('Please, enter the name of file for publication ')
    if kind_of_publication == 'News':
        create_news().publish(file_name)
    elif kind_of_publication=='Private ad':
        create_private_ad().publish(file_name)
    elif kind_of_publication=='Restaurant Review':
        create_restaurant_review().publish(file_name)
    else:
        raise ValueError('Type of publication should be News, Private ad or Restaurant Review')

def create_news():
    text = input("Please, enter the text ")
    city = input("Please, enter the city ")
    a = News(text, city)
    return a

def create_private_ad():
    text = input("Please, enter the text ")
    expiration_date = input("Please, enter expiration date in format YYYY-MM-DD ")
    b = PrivateAd(text, expiration_date)
    return b

def create_restaurant_review():
    text = input("Please, enter the text ")
    rating = input("Please, enter rating ")
    c = RestaurantReview(text, rating)
    return c




