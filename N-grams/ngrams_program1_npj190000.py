# Nick Johnson
# CS 4395.001
# Ngrams Program 1

import pickle
import pathlib
from nltk import word_tokenize
from nltk.util import ngrams


def dict_gen(filename):  # create a function with a filename as argument
    file = open(pathlib.Path.cwd().joinpath(filename), 'r')  # read from specified filepath
    raw_text = file.read()
    raw_text = raw_text.replace('\n', '')  # remove newlines
    raw_text_tokens = word_tokenize(raw_text)  # tokenize the text
    bigrams = list(ngrams(raw_text_tokens, 2))  # use nltk to create a bigrams list
    unigrams = list(ngrams(raw_text_tokens, 1))  # use nltk to create a unigrams list
    bigram_dict = {b:bigrams.count(b) for b in set(bigrams)}  # create bigrams dictionary of bigrams and counts
    unigram_dict = {u:unigrams.count(u) for u in set(unigrams)}  # create unigrams dictionary of unigrams and counts
    return unigram_dict, bigram_dict  # return unigram dictionary and bigram dictionary


if __name__ == "__main__":
    u_d, b_d = dict_gen('data/LangId.train.English')  # dict_gen call for English
    pickle.dump(u_d, open('pickled_dicts/English_Unigram_Dict.pickle', 'wb'))  # pickling English unigram dict
    pickle.dump(b_d, open('pickled_dicts/English_Bigram_Dict.pickle', 'wb'))  # pickling English bigram dict

    u_d, b_d = dict_gen('data/LangId.train.French')  # dict_gen call for French
    pickle.dump(u_d, open('pickled_dicts/French_Unigram_Dict.pickle', 'wb'))  # pickling French unigram dict
    pickle.dump(b_d, open('pickled_dicts/French_Bigram_Dict.pickle', 'wb'))  # pickling French bigram dict

    u_d, b_d = dict_gen('data/LangId.train.Italian')  # dict_gen call for Italian
    pickle.dump(u_d, open('pickled_dicts/Italian_Unigram_Dict.pickle', 'wb'))  # pickling Italian unigram dict
    pickle.dump(b_d, open('pickled_dicts/Italian_Bigram_Dict.pickle', 'wb'))  # pickling Italian bigram dict
