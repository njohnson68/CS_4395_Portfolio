# Nick Johnson
# CS 4395.001
# Ngrams Program 2

import pickle
from nltk import word_tokenize
from nltk.util import ngrams


def prob_calc(test_file_bigrams, unigram_dict, bigram_dict, vocab_size):
    # Probability for each bigram with Laplace smoothing: (b + 1) / (u + v)
    # b = bigram count
    # u = unigram count of first word in the bigram
    # v = total vocabulary size
    probability = 1  # initializing probability to 1
    for bigram in test_file_bigrams:   # iterate through each bigram in test_file_bigrams
        if bigram[0] in unigram_dict:  # if first word in bigram is in unigram_dict
            u = unigram_dict[bigram[0]]  # u equals count of that word in the unigram_dict
        else:  # if first word in bigram not in unigram_dict
            u = 0  # u equals 0
        if bigram in bigram_dict:  # if the bigram is found in the bigram_dict
            b = bigram_dict[bigram]  # b equals the count of the bigram in the bigram_dict
        else:  # if the bigram is not found in the bigram_dict
            b = 0  # b equals 0
        probability *= ((b + 1) / (u + vocab_size))  # multiplying each of the probabilities together
    return probability  # return the final probability


if __name__ == '__main__':
    engU = pickle.load(open('pickled_dicts/English_Unigram_Dict.pickle', 'rb'))  # read in pickled English unigram dict
    engB = pickle.load(open('pickled_dicts/English_Bigram_Dict.pickle', 'rb'))  # read in pickled English bigram dict
    freU = pickle.load(open('pickled_dicts/French_Unigram_Dict.pickle', 'rb'))  # read in pickled French unigram dict
    freB = pickle.load(open('pickled_dicts/French_Bigram_Dict.pickle', 'rb'))  # read in pickled French bigram dict
    itaU = pickle.load(open('pickled_dicts/Italian_Unigram_Dict.pickle', 'rb'))  # read in pickled Italian unigram dict
    itaB = pickle.load(open('pickled_dicts/Italian_Bigram_Dict.pickle', 'rb'))  # read in pickled Italian bigram dict

    results_file = open('data/LangId.results', 'w')  # open a results file for writing
    test_file = open('data/LangId.test', 'r').readlines()  # read in the test file
    solution_file = open('data/LangId.sol', 'r').readlines()  # read in the solution file

    # total vocab size is equal to the sum of the length of the 3 unigram dicts
    total_vocab_size = len(engU) + len(freU) + len(itaU)

    incorrect_line_numbers = []  # creating a list to hold the line numbers of incorrectly classified items
    number_of_incorrect = 0  # tracking how many items are incorrectly classified to use later for calculating accuracy
    lineNumber = 1  # need this to be able to write the correct line number to the results file

    for line in test_file:  # for each line in the test file

        line_tokens = word_tokenize(line)  # tokenize the line
        bigrams = list(ngrams(line_tokens, 2))  # get bigrams of the line

        engProbability = prob_calc(bigrams, engU, engB, total_vocab_size)  # calculate English probability
        freProbability = prob_calc(bigrams, freU, freB, total_vocab_size)  # calculate French probability
        itaProbability = prob_calc(bigrams, itaU, itaB, total_vocab_size)  # calculate Italian probability

        if engProbability > max(freProbability, itaProbability):  # if English probability highest
            language = "English"  # set language variable to English
        elif freProbability > max(engProbability, itaProbability):  # if French probability highest
            language = "French"  # set language variable to French
        elif itaProbability > max(engProbability, freProbability):  # if Italian probability highest
            language = "Italian"  # set language variable to Italian
        else:  # if none are highest
            language = "?"  # set language variable to question mark

        # write line number and language with the highest probability to the results file
        results_file.write(str(lineNumber) + " " + language + "\n")

        # Check if classification is correct by comparing with the solution file
        if solution_file[lineNumber - 1] != str(str(lineNumber) + " " + language + "\n"):
            incorrect_line_numbers.append(lineNumber)  # append line number for each incorrect classification
            number_of_incorrect += 1  # add 1 to number of incorrect classifications

        lineNumber += 1  # iterate through each line

    accuracy_percentage = ((300 - number_of_incorrect) / 300) * 100  # calculate the accuracy
    print("Accuracy: " + str(accuracy_percentage) + "%")  # output accuracy
    print("Line Numbers of Incorrectly Classified Items: " + str(incorrect_line_numbers))  # output line numbers
