# CS_4395_Portfolio
Portfolio for CS 4395 (Human Language Technologies) class work

## Overview of NLP
[Document](Overview_of_NLP.pdf) that summarizes historical and current approaches to NLP, as well as reflects on my own personal interest in NLP.

## Homework 1: Text Processing with Python

### Program Description
[This program](Homework1/Homework1_npj190000.py) reads in an employee file that was created on an obsolete system, processes the text to be more standardized, creates an object for each person using the corrections given by the user, and outputs each person’s now-standardized information.

### How to Run the Program
I used PyCharm to do this assignment. To run it in PyCharm, you first need to edit the configuration for the python file. Once you see the configuration, you need to edit the parameters so that it says ‘data/data.csv’. From there, you can run the program as normal.

### Strengths/Weaknesses of Using Python for Text Processing
Python’s simpler syntax makes it easier to write programs like this one to do text processing. Having to use regex while doing text processing isn’t the easiest, but it is effective at pattern matching.

### What I Learned in this Assignment
I’m still pretty new to Python, so this was all a learning experience for me. This assignment allowed me to practice doing things in Python like creating a class, using pickle, and taking in user input.

## Homework 2: Word Guessing Game
[This program](Homework2/homework2_npj190000.py) uses Python and NLTK features to explore a text file and create a word guessing game. 

## WordNet
[This](portfolio_assignment_wordnet_npj190000.pdf) is the PDF of my WordNet assignment which was originally created as a Jupyter Notebook. This assignment allowed me to gain familiarity with using WordNet and SentiWordNet. It also allowed me to learn how to identify collocations.

## N-grams
In [this](N-grams) assignment, I created unigram and bigram dictionaries for English, French, and Italian using the provided training data where the key is the unigram or bigram text and the value is the count of that unigram or bigram in the data. Then for the test data, I calculated probabilities for each language and compared against the true labels. Also included is a one-page narrative about n-grams.
