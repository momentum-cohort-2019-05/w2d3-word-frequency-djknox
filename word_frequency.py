# word_frequency.py will read a file and:
# - remove punctuation
# - normalize all words to lowercase
# - remove "stop words" -- words used so frequently they are ignored
# - go through the file word by word and keep a count of how often each word is used

# import string_cleaner function for cleaning up string
from string_cleaner import strip_new_lines_punctuation_and_make_lowercase 

def remove_stop_words(phrase):
    """Create a list containing each word in phrase and remove 'stop words' from that list"""
    STOP_WORDS = [
        'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
        'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
        'will', 'with'
    ]
    # split into list with each word as element in that list
    phrase = phrase.split()
    # remove element in list if exists in STOP_WORDS
    phrase_without_stop_words = []
    for word in phrase:
        if word not in STOP_WORDS:
            phrase_without_stop_words.append(word)
    return phrase_without_stop_words

def count_frequency_of_words_in_list(a_list):
    word_frequencies = {}
    #loop through each word
    #if the word is not a key, then create the key with a value of 1
    #if the word is already a key, then increment the value
    for word in a_list:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] = word_frequencies[word] + 1
    return word_frequencies

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # open file
    with open(file) as seneca_falls:
        seneca_falls = seneca_falls.read()
        # remove punctuation
        seneca_falls = strip_new_lines_punctuation_and_make_lowercase(seneca_falls)
        # remove stop words
        seneca_falls = remove_stop_words(seneca_falls)
        # count frequency of each word
        word_frequencies = count_frequency_of_words_in_list(seneca_falls)
        # sort word_frequencies by the keys
        word_frequencies = sorted(word_frequencies.items())
        # sort word_frequencies by the values
        word_frequencies = sorted(word_frequencies, key=lambda x: x[1], reverse=True)
        # print out an asterisk for each occurence of the word and right-justify output
        for word, frequency in word_frequencies[0:10]:
            print(f"{word:>8} | {frequency}", "*" * frequency)

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
