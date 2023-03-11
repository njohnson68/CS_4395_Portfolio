# Nick Johnson
# CS 4395.001
# npj190000
# Web Crawler

from bs4 import BeautifulSoup  # used in the web_crawler and loop_and_scrape functions
import requests  # used in the web_crawler function
from nltk.corpus import stopwords  # used in the extract_important function to remove stopwords
from nltk import word_tokenize  # used in the extract_important function as part of the punctuation removal process
from nltk import sent_tokenize  # used in the clean_up function to extract sentences
from urllib import request  # used in the loop_and_scrape function
import pickle  # used throughout the program for storing text
from os import listdir  # used for getting list of files in clean_up and extract_important functions
from os.path import isfile  # used for getting list of files in clean_up and extract_important functions
from os.path import join  # used for getting list of files in clean_up and extract_important functions
import re  # used for removing punctuation in extract_important function
from nltk.probability import FreqDist  # used to get important words in extract_important function


def web_crawler(starter_url):
    crawled_links = []  # keeping track of links we've crawled
    queue = [starter_url]  # creating queue
    visited_links = 0  # starting with 0 visited links
    max_links = 15  # cutoff for max links, for this program I am choosing 15 as the max
    while visited_links < max_links and queue:  # as long as we haven't gotten all 15 links yet and queue isn't empty
        url = queue.pop(0)  # pop the first element in the queue

        r = requests.get(url)

        data = r.text
        soup = BeautifulSoup(data, "lxml")  # specifying parser here to get rid of long warning thrown by beautiful soup

        crawled_links.append(url)
        visited_links += 1
        for link in soup.find_all('a'):
            link_str = str(link.get('href'))
            if 'Dallas' in link_str or 'dallas' in link_str:  # accept keys here are 'Dallas' and 'dallas'
                if link_str.startswith('/url?q='):
                    link_str = link_str[7:]
                if '&' in link_str:
                    i = link_str.find('&')
                    link_str = link_str[:i]
                if link_str.startswith('http'):
                    # make sure link wasn't crawled earlier and is not currently in the queue
                    if link_str not in crawled_links and link_str not in queue:
                        queue.append(link_str)
    print("15 URLs:")
    print(crawled_links)  # printing our 15 crawled urls
    return crawled_links  # returning our crawled urls to use in the loop_and_scrape function


def loop_and_scrape(link_list):
    for url in link_list:  # loop through each link
        html = request.urlopen(url).read().decode('utf8')
        soup = BeautifulSoup(html, "lxml")  # specifying parser here to get rid of long warning thrown by beautiful soup
        for script in soup(['script', 'style']):  # extracting all scripts and styles
            script.extract()
        text = soup.get_text()  # extracting text
        # Pickle the text for the link
        pickle.dump(text, open('scraped_text/scraped_text{}.txt'.format(link_list.index(url) + 1), 'wb'))


def clean_up():
    # Get the list of scraped_text files so that we can clean them up in this function
    scraped_text_files = [f for f in listdir('scraped_text') if isfile(join('scraped_text', f))]
    for file in scraped_text_files:  # loop through each file in our list of scraped_text files
        text = pickle.load(open('scraped_text/{}'.format(file), 'rb'))  # Unpickle the file
        # Removing newline and tab characters
        text = text.replace('\n', '').replace('\t', '')
        sents = sent_tokenize(text)  # extract sentences with nltk's sentence tokenizer
        # Pickle the now-cleaned-up sentences into a file
        pickle.dump(sents, open('cleaned_up_sentences/cleaned_up_sentences{}.txt'.format(scraped_text_files.index(file) + 1), 'wb'))


def extract_important():
    # Get the list of cleaned_up_sentences files so that we can extract important words from each of them
    cleaned_up_files = [f for f in listdir('cleaned_up_sentences') if isfile(join('cleaned_up_sentences', f))]
    print("Important Words:")
    for file in cleaned_up_files:   # loop through each file in our list of cleaned_up_sentences files
        text = pickle.load(open('cleaned_up_sentences/{}'.format(file), 'rb'))  # Unpickle the file
        tokens = []  # initializing our list of tokens
        for sentence in text:  # go through each sentence in the unpickled file
            sent = re.sub(r'[^\w\s]', '', sentence)  # removing punctuation
            tokens += word_tokenize(sent)  # tokenizing the words in improved sentences and adding to our list of tokens
        remove_stop_and_make_lower = [t.lower() for t in tokens if t not in stopwords.words('english')]
        # removing stopwords and making the tokens lowercase in the line above
        fd = FreqDist(remove_stop_and_make_lower)  # running a frequency distribution on our improved tokens
        important_words = fd.most_common(30)  # extracting the top 30 important words
        print(important_words)  # printing those important words
        print()  # help make the lists of words more readable


def knowledge_base():
    # creating a knowledge base dict of term : fact for 10 terms
    base = {
        'NHL': 'The NHL, or the National Hockey League, is the league that the Dallas Stars play in.',
        'hockey': 'Hockey is a sport played on ice between two teams each with five skaters and a goalie.',
        'Modano': 'Mike Modano is the all-time goals and points leader for American-born players in NHL history.',
        'relocation': 'The Dallas Stars relocated from Minnesota when they were known as the North Stars in 1993.',
        'Stanley': 'The Dallas Stars won the Stanley Cup in 1999.',
        'American': 'The Dallas Stars play their home games in the American Airlines Center in downtown Dallas.',
        'Western': 'The Dallas Stars play in the Western Conference of the NHL. ',
        'captain': 'The current captain of the Dallas Stars is Jamie Benn.',
        'AHL': 'The AHL affiliate of the Dallas Stars is the Texas Stars.',
        'Reunion': 'The Dallas Stars played home games at Reunion Arena from 1993 to 2001.'
    }
    pickle.dump(base, open('knowledge_base', 'wb'))  # pickling our knowledge base dict


if __name__ == '__main__':
    # My starter url of choice for this program is the Dallas Stars Wikipedia page
    list_of_links = web_crawler("https://en.wikipedia.org/wiki/Dallas_Stars")  # run the web_crawler function
    loop_and_scrape(list_of_links)  # run loop_and_scrape on the returned links from the web_crawler function
    clean_up()  # run the clean_up function
    extract_important()  # run the extract_important function
    knowledge_base()  # run the knowledge_base function
