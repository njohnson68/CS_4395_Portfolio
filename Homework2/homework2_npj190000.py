# Homework 2
# Nick Johnson
# npj190000
# CS 4395.001
import sys
from nltk import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import operator
from random import randint
import time


def lexical_diversity(input_file):
    file_words = open(input_file).read()  # open the file for reading
    tokens = word_tokenize(file_words)  # tokenize the contents of the file
    total_tokens = len(tokens)  # total number of tokens
    total_unique_tokens = len(set(tokens))  # total number of unique tokens
    lex_diversity = total_unique_tokens / total_tokens  # calculate lexical diversity
    print("Lexical diversity: " + "%.2f" % lex_diversity)  # printing lexical diversity to 2 decimal places


def preprocess(input_file):
    file_words = open(input_file).read()  # open the file for reading
    stop_words = stopwords.words('english')  # defining stop_words
    reduced = [t.lower() for t in word_tokenize(file_words) if t.isalpha() and t not in stop_words and len(t) > 5]
    # reduced is the list of lowercase tokens that are alpha, not in stop_words, and have length > 5
    wnl = WordNetLemmatizer()  # creating a lemmatizer
    lemmas = [wnl.lemmatize(t) for t in reduced]  # lemmatizing the reduced tokens
    unique_lemmas = set(lemmas)  # making a list of unique lemmas using set()
    pos_tags = pos_tag(unique_lemmas)  # pos tagging the unique lemmas
    print("\nFirst 20 tagged words: ", pos_tags[0:20])  # printing the first 20 tagged unique lemmas
    nouns = [item[0] for item in pos_tags if item[1][0] == 'N']  # creating a list of nouns
    print("Number of tokens after preprocessing: ", len(reduced))  # printing number of reduced tokens
    print("Number of nouns after preprocessing: ", len(nouns))  # printing number of nouns
    return reduced, nouns


def guessing_game():
    print("\nLet's play a word guessing game!")  # beginning the word guessing game
    points = 5  # giving the user 5 points to start with
    random_num = randint(1, 50)  # generate a random int between 1 and 50, both included
    secret_word = common_words[random_num - 1]
    # assign the secret word to be the common word at the randomly chosen index, subtracting 1 since lists start from 0
    underscores = list("_" * len(secret_word))  # creating the list of underscores with length equal to the secret_word
    print(' '.join(underscores))  # printing the underscores, one for each letter in the secret word
    user_guess = input("Guess a letter: ")  # initial prompting of the user to guess a letter
    while user_guess != "!":  # as long as the user doesn't input '!' as their guess

        if len(user_guess) > 1 or user_guess == "":  # making sure guess is exactly one letter
            print("Please enter a single letter.")
            time.sleep(1)
            user_guess = input("Guess a letter: ")
        else:

            if user_guess in secret_word:  # if the guess is in the secret word
                i = 0
                while i < len(secret_word):  # filling in blanks with correct letter in correct places
                    if user_guess == secret_word[i]:
                        underscores[i] = user_guess
                    i += 1
                if underscores == list(secret_word):  # if the word has now been solved
                    points += 1  # give the user a point
                    print("You solved it! Score is", points)  # tell user they solved the word, show points total
                    time.sleep(1)
                    print(' '.join(underscores))  # print solved word
                    time.sleep(1)
                    print("Congratulations!")  # give the user congratulations
                    time.sleep(1)
                    quit()
                else:  # if the word is still only partially solved
                    points += 1  # give the user a point
                    print("Right! Score is", points)  # indicate a correct guess, show the current points total
                    time.sleep(1)
                    print(' '.join(underscores))  # print the updated partially filled in word
                    time.sleep(1)
                    user_guess = input("Guess a letter: ")  # allow user to guess again
            if user_guess not in secret_word:  # if the guess is not in the secret word
                points -= 1  # subtract a point from the user
                if points > -1:  # if the total score is not negative, allow user to guess again
                    print("Sorry, guess again. Score is", points)  # inform user of incorrect guess, show points total
                    time.sleep(1)
                    print(' '.join(underscores))  # show the current progress of filling in the word
                    time.sleep(1)
                    user_guess = input("Guess a letter: ")  # allow user to guess again
                else:  # handling a negative score
                    print("Score is", points)  # display points total
                    time.sleep(1)
                    print(' '.join(underscores))  # show final progress of filling in the word
                    time.sleep(1)
                    print("The word was ")  # tell user
                    time.sleep(1)
                    print(secret_word)  # what the secret word was
                    time.sleep(1)
                    print("Game over")  # let the user know the game has ended
                    time.sleep(1)
                    quit()  # end the program


if __name__ == '__main__':
    # file name
    if len(sys.argv) > 1:  # sysarg is present
        arg_input = sys.argv[1]  # getting arg input
        print('Input file: ', arg_input)  # printing the file name
        lexical_diversity(arg_input)  # calculating lexical diversity of the input file
        reduced, nouns = preprocess(arg_input)  # getting reduced tokens and nouns lists from the preprocess function
        dictionary = {}  # creating the dictionary
        for noun in nouns:  # making the dictionary with (noun: count of noun in tokens) items
            dictionary[noun] = reduced.count(noun)
        sorted_dictionary = dict(sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)[0:50])
        # sorting the dictionary by count and getting 50 most common words and their counts in the line above
        common_words = list(sorted_dictionary.keys())  # saving the 50 most common words in a list to use for game
        print("\n50 most common words:")  # printing the 50 most common words and their counts
        for key, value in sorted_dictionary.items():
            print(key, ",", value)
        guessing_game()  # calling the guessing game function to let the user play the game
    else:  # if no sysarg present
        print('File name missing')  # print error message
    print('\nProgram ended')  # end the program
