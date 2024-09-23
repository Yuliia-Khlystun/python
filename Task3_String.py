import re

text = """homEwork:
	tHis iz your homeWork, copy these Text to variable.

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# Normalize and correct misspellings in the text
replaced_iz = text.lower().replace(" iz ", " is ").capitalize()

# Capitalize the first letter of each sentence:
def capitalize_first_letter(match):
    return match.group(0).upper()
capitalized_text = re.sub(r'(?<=[.!?\n]\s)(\w)', capitalize_first_letter, replaced_iz)

# Count all whitespace characters in the text
whitespaces = re.findall(r'\s', capitalized_text)
count_whitespaces = len(whitespaces)
print(count_whitespaces)

# Forming a new sentence from the last word of each existing sentence
last_words = re.findall(r'\b(\w+)\b(?=[.?!])', capitalized_text)
new_sentence = ' '.join(last_words)+'.'
capitalized_text+= ' ' + new_sentence.capitalize()

# Output the modified text
print(capitalized_text)
