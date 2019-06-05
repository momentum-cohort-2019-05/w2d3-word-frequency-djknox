# string_cleaner.py contains a function for making a string lowercase and stripping the whitespace and punctuation

# import re library for using regular expressions
import re

def strip_whitespace_and_punctuation_and_make_lowercase(phrase):
    """remove all characters except for alphabetical letters from a string and make lowercase"""
    phrase = re.sub(r'[^A-Za-z]', '', phrase)
    return phrase.lower()

def strip_new_lines_punctuation_and_make_lowercase(phrase):
    # make lowercase
    phrase = phrase.lower()
    # replace line breaks with spaces
    phrase = phrase.replace('\n', ' ')
    # replace dashes with spaces
    phrase = phrase.replace('-', ' ')
    # remove everything but lowercase alphas and spaces
    phrase = re.sub(r'[^a-z\s]', '', phrase)
    return phrase