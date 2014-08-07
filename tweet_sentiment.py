'''
compute the sentiment of each tweet based on the sentiment scores of the terms 
in the tweet. The sentiment of a tweet is equivalent to the sum of the sentiment
 scores for each term in the tweet.
'''

import sys
import json

# prints the number of lines in a file
def lines(fp):
    print str(len(fp.readlines()))

# Calculate sentiment for each tweet
def tweet_sentiment(sent_file, tweet_file):
    tweet_scores = {} # initialize empty dictionary
        
    for line in sent_file:  # fill in keys and scores
        term, score = line.split('\t') # file is tab-delimited
        tweet_scores[term] = int(score) # convert the score to integer type
    
    tweet_list = [] # initialize empty list
       
    for line in tweet_file:
        # only choose english tweets
        if('lang' in line and json.loads(line)['lang'] is 'en'):        
            # parse the json data and return a python data stucture(dict)
            tweet_list.append(json.loads(line)['text'])

    for tweet in tweet_list:
        
        # initialize sentiment for each tweet
        sentiment_score = 0
        
        # sum up total each tweet's sentiment
        for word in tweet.split(' '):
            
            sentiment_score += tweet_scores.get(word, 0) 

        print sentiment_score

def main():
    # hw()
    
    # lines(sent_file)
    
    # lines(tweet_file) 
    
    sent_file = open(sys.argv[1])
    #sent_file = open('AFINN-111.txt') # use this for local machine   
    
    tweet_file = open(sys.argv[2])
    #tweet_file = open('output.txt') # use this for local machine
    
    tweet_sentiment(sent_file, tweet_file)
    
    sent_file.close()
    
    tweet_file.close() 
           
if __name__ == '__main__':
    main()
