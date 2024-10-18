from Task6.Task4_functions import normalize_misspellings, capitalize_text, count_whitespaces, add_sentence, \
    generate_list_of_dicts, aggregate_keys, create_common_dict

text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""
replaced_iz = normalize_misspellings(text, ' iz ', ' is ')
capitalized_text = capitalize_text(replaced_iz)
count_whitespaces(capitalized_text)
print(f"There are {count_whitespaces(capitalized_text)} all whitespace characters in the text")
result = add_sentence(capitalized_text)
print(f"Text after adding new sentence from the last word of each existing sentence: "
        f"{result}")

dict_list = generate_list_of_dicts(2, 10)
print("List of dictionaries:")
for i in dict_list:
    print(i)
keys_of_common_dict = aggregate_keys(dict_list)
dict_tuple = tuple(dict_list)
common_dict = create_common_dict(dict_tuple, keys_of_common_dict)
print("common dict", common_dict)



