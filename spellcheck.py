###
### Author: Hung Le Ba
### Description: The program takes a text file as input
###             and allow user to choose between "replace"
###             and "suggest" mode. It then compare and find
###             misspell words with the text. Next, replace it or
###             print a suggest list depends on the type of mode.
###
import string

def text_to_dictionary():
    '''
    Convert the 'Common_misspelled_words.txt' file (already provided)
    into a complete dictionary for easier comparision
    '''
    dictionary = {}
    lines = open('Common_misspelled_words.txt', 'r').readlines()
    for line in lines:
        line = line.strip('\n').replace(':', ',').split(',')
        for i in range(len(line)-1):
            dictionary[line[i+1]] = line[0]
    return dictionary

def check_misspell_word(word, dictionary):
    '''
    Take 2 parameter: a word, and a dictionary.
    The function will have a check in the dictionary,
    if the word is misspell, the function will
    return the correct word!
    '''
    for key in dictionary:
        val = dictionary[key]
        if key == word:
            return val
    return word

def replace(file_name, dictionary):
    '''
    This function will immediately replace
    every misspelling words in the text
    '''
    lines = open(file_name, 'r').readlines()
    correct_text = '\n--- OUTPUT ---\n'
    for line in lines:
        line = line.strip('\n').split(' ')
        for word in line:
            if word != '':
                #is_upper > 0 when first character is capitalized
                is_upper = 0
                punctuation = ''
                #check capitalization and punctuation
                word, is_upper = handle_capitalization(word, is_upper)
                word, punctuation = handle_punctuation(word, punctuation)

                #check if it's misspelling word and replace
                correct_word = check_misspell_word(word, dictionary)
                if word != correct_word:
                    word = correct_word
                if is_upper > 0:
                    word = word.replace(word[0], word[0].capitalize(),1)

                correct_text += (word+punctuation+' ')
        correct_text += '\n'
    print(correct_text)

def handle_capitalization(word, is_upper):
    '''
    Check if the first character is capitalized,
    if yes, convert it into a lower one
    Parameter: is_upper(if >0, it means the character
    is capitalized)
    '''
    if word[0].isupper() == True:
        word = word.replace(word[0], word[0].lower())
        is_upper += 1
    return word, is_upper

def handle_punctuation(word, punctuation):
    '''
    Check if the word has punctuation. If yes,
    store it in a variable and return it.
    '''
    if word[-1] in string.punctuation:
        punctuation = word[-1]
        word = word.replace(word[-1], '')
    return word, punctuation

def get_correct_text(correct_text, is_incorrect,
word, punctuation, incorrect_index):
    '''
    Take essential parameter, concatenate those into
    complete correct output text.
    Parameter: is_incorrect(true if the word is incorrect)
    incorrect_index(the index number of incorrect words)
    '''
    if is_incorrect == False:
        correct_text += (word+punctuation+' ')
    elif is_incorrect == True:
        correct_text += \
        (word+punctuation+' '+'('+str(incorrect_index)+') ')
    return correct_text

def get_legend(legend, is_incorrect, incorrect_index,
correct_word, is_upper):
    '''
    Take essential parameter, concatenate those into
    complete correct output suggest text.
    '''
    if is_incorrect == True:
        if is_upper > 0:
            correct_word = correct_word.replace\
            (correct_word[0], correct_word[0].capitalize())
            legend += '('+str(incorrect_index)+') '+correct_word+'\n'
        else:
            legend += '('+str(incorrect_index)+') '+correct_word+'\n'
    return legend


def suggest(file_name, dictionary):
    '''
    Almost same function as "replace", the difference is instead of
    replacing, it print out the suggestion for misspelling words
    '''
    lines = open(file_name, 'r').readlines()
    correct_text = '\n--- OUTPUT ---\n'
    legend ='--- LEGEND ---\n'
    incorrect_index = 0
    for line in lines:
        line = line.strip('\n').split(' ')
        for word in line:
            if word != '':
                is_incorrect = False
                is_upper = 0
                punctuation = ''
                word, is_upper = handle_capitalization(word, is_upper)
                word, punctuation = handle_punctuation(word, punctuation)
                correct_word = check_misspell_word(word, dictionary)
                if word != correct_word:
                    incorrect_index += 1
                    is_incorrect = True
                if is_upper > 0:
                    word = word.replace(word[0], word[0].capitalize(),1)
                correct_text = get_correct_text(correct_text, is_incorrect,
                word, punctuation, incorrect_index)
                legend = get_legend(legend, is_incorrect, incorrect_index,
                correct_word, is_upper)
        correct_text += '\n'
    print(correct_text+'\n'+legend)

def main():
    '''
    Take the user's input of text file name and
    mode name, call other functions to print out
    the complete correct output
    '''
    dictionary = text_to_dictionary()
    file_name = input('Enter input file: \n')
    mode = input('Enter spellcheck mode (replace or suggest):\n')
    if mode == 'replace':
        replace(file_name, dictionary)
    elif mode == 'suggest':
        suggest(file_name, dictionary)

main()
