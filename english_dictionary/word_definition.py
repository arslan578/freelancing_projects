from difflib import get_close_matches, SequenceMatcher
import json


def dictionary_word_definition(word):
    data = json.load(open("data.json"))
    word = word.lower()
    if word in data:
        return "%s " % data[word]

    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        close_matches_words = get_close_matches(word, data.keys(), cutoff=0.8)
        ask_user_about_word = input("Do you mean %s? if yes type 'Y' and otherwise type 'N': " % close_matches_words[0])
        if ask_user_about_word.upper() == 'Y':
            return "%s " % data[close_matches_words[0]]
        elif ask_user_about_word.upper() == 'N':
            return "Does not find any word"

        else:
            return "Does not understand your decision"

    else:
        return "Word does not exist"


flag = True

while True:
    if flag:
        input_word = dictionary_word_definition(input("Please enter the word: "))
        print(input_word)
    ask_user_to_continue = input("Do you want to continue: Type 'Y' otherwise type 'N': ")
    if ask_user_to_continue.upper() == 'Y':
        input_word = dictionary_word_definition(input("Please enter the word: "))
        print(input_word)
        flag = False
    else:
        break
