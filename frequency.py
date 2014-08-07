import sys
import json

def hw():
    print 'Hello, world!'

# Prints the number of lines in a file
def lines(fp):
    print str(len(fp.readlines()))

# Calculate sentiment for each tweet
def tweet_frequency(tweet_file):        
    tweet_list = [] # initialize empty list
    
    # collect all the tweets into a list
    for line in tweet_file:
        # only choose english tweets
        if('lang' in line and json.loads(line)['lang'] is 'en'):        
            # parse the json data and return a python data stucture(dict)
            tweet_list.append(json.loads(line)['text'])
    
    # find each unique term's occurence
    tweet_freq = {} # initialize empty dictionary
    for tweet in tweet_list:       
        
        for word in tweet.split():
            
            if(tweet_freq.get(word, 0) == 0): 
                
                tweet_freq.update({word : 1})
                
            else:
                
                tweet_freq[word] += 1
                
    # sum up all terms' occurences           
    total_occurence = sum(tweet_freq.itervalues())           
                
    for key, value in tweet_freq.iteritems():
        
        print key, float(value) / float(total_occurence)
        
def test(tweet_file):
    tweet_list = []
    for line in tweet_file:
        tweet_list.append(line)
    tweet_freq = {} # initialize empty dictionary
    for tweet in tweet_list:               
        for word in tweet.split():            
            if(tweet_freq.get(word, 0) == 0):                
                tweet_freq.update({word : 1})                
            else:                
                tweet_freq[word] += 1                
    # sum up all terms' occurences           
    total_occurence = sum(tweet_freq.itervalues())               
    print tweet_freq            
    for key, value in tweet_freq.iteritems():        
        print key, float(value) / total_occurence
        
        
def main():
    
    # hw()
    
    # lines(sent_file)
    
    # lines(tweet_file)
    
    tweet_file = open(sys.argv[1])
    #tweet_file = open('output.txt') # use this for local machine
    
    tweet_frequency(tweet_file)
    
    # test(open('test.txt'))
    
    tweet_file.close()   
    
if __name__ == '__main__':
    main()
    