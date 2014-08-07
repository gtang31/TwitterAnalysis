# -*- coding: utf-8 -*-
"""
Created on Wed Aug 06 23:54:42 2014

@author: GLT

Finds the top (10) tweeted hash-tags in twitter.
"""

import sys
import json
from collections import Counter # use this module to keep track of unique elements

def get_hashtags(tweet_file):
    hashtag_list = []
    
    for line in tweet_file:
        
        if('entities' in line and json.loads(line)['entities']['hashtags']):
            
            hashTags = json.loads(line)['entities']['hashtags']
            
            hashtag_list += [hashTags[i]['text'] for i in range(len(hashTags))]
            
            #hashtag_list.append(json.loads(line)['entities'])
    
    # returns a list of tuples countain the hashtag-count pair
    top_hashtags = Counter(hashtag_list).most_common(10)
    
    for wordCountPair in top_hashtags:
        
        print wordCountPair[0], wordCountPair[1]
    
def main():
    
    tweet_file = open(sys.argv[1])
    
    #tweet_file = open('output1.txt')
    
    get_hashtags(tweet_file)
    
    tweet_file.close()
    
if __name__ == '__main__':
    main()