import re


def normalize_misspellings (text, old, new):
    # Normalize and correct misspellings in the text
    replaced_iz = text.lower().replace(old, new).capitalize()
    return replaced_iz

# Capitalize the first letter of each sentence:
def capitalize_first_letter(match):
    return match.group(0).upper()
def capitalize_text (text):
    capitalized_text = re.sub(r'(?<=[.!?\n]\s)(\w)', capitalize_first_letter, text)
    return capitalized_text

# Count all whitespace characters in the text
def count_whitespaces(text):
    whitespaces = re.findall(r'\s', text)
    count_whitespace = len(whitespaces)
    print(f"There are {count_whitespace} all whitespace characters in the text")
    return count_whitespace

# Form a new sentence from the last word of each existing sentence
def add_sentence (text):
    last_words = re.findall(r'\b(\w+)\b(?=[.?!])', text)
    new_sentence = ' '.join(last_words) + '.'
    text += ' ' + new_sentence.capitalize()
    return text

def main(text):
    replaced_iz = normalize_misspellings(text, 'iz', 'is')
    capitalized_text = capitalize_text(replaced_iz)
    count_whitespaces(capitalized_text)
    result = add_sentence(capitalized_text)
    print(f"Text after adding new sentence from the last word of each existing sentence: "
          f"{result}")
    return result

text = """homEwork:
    	tHis iz your homeWork, copy these Text to variable.

    	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

    	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

    	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""
main(text)

