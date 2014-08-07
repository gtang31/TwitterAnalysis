'''
Find the state with the happiest tweets
'''

import sys
import json

# Calculate sentiment for each tweet
def tweet_sentiment(tweet_scores, tweet):
    sentiment_score = 0
    
    # sum up total each tweet's sentiment
    for word in tweet.split():
        
        sentiment_score += tweet_scores.get(word, 0) 

    return sentiment_score

# prints the number of lines in a file
def lines(fp):
    print str(len(fp.readlines()))

# Determine which state has the happiest tweets
def happy_state(sent_file, tweet_file):
    states = {
                'AK': 'Alaska',
                'AL': 'Alabama',
                'AR': 'Arkansas',
                'AS': 'American Samoa',
                'AZ': 'Arizona',
                'CA': 'California',
                'CO': 'Colorado',
                'CT': 'Connecticut',
                'DC': 'District of Columbia',
                'DE': 'Delaware',
                'FL': 'Florida',
                'GA': 'Georgia',
                'GU': 'Guam',
                'HI': 'Hawaii',
                'IA': 'Iowa',
                'ID': 'Idaho',
                'IL': 'Illinois',
                'IN': 'Indiana',
                'KS': 'Kansas',
                'KY': 'Kentucky',
                'LA': 'Louisiana',
                'MA': 'Massachusetts',
                'MD': 'Maryland',
                'ME': 'Maine',
                'MI': 'Michigan',
                'MN': 'Minnesota',
                'MO': 'Missouri',
                'MP': 'Northern Mariana Islands',
                'MS': 'Mississippi',
                'MT': 'Montana',
                'NA': 'National',
                'NC': 'North Carolina',
                'ND': 'North Dakota',
                'NE': 'Nebraska',
                'NH': 'New Hampshire',
                'NJ': 'New Jersey',
                'NM': 'New Mexico',
                'NV': 'Nevada',
                'NY': 'New York',
                'OH': 'Ohio',
                'OK': 'Oklahoma',
                'OR': 'Oregon',
                'PA': 'Pennsylvania',
                'PR': 'Puerto Rico',
                'RI': 'Rhode Island',
                'SC': 'South Carolina',
                'SD': 'South Dakota',
                'TN': 'Tennessee',
                'TX': 'Texas',
                'UT': 'Utah',
                'VA': 'Virginia',
                'VI': 'Virgin Islands',
                'VT': 'Vermont',
                'WA': 'Washington',
                'WI': 'Wisconsin',
                'WV': 'West Virginia',
                'WY': 'Wyoming'
                }    
    
    state_scores = {} # dictionary to hold each state's happiness score
    
    for key in states.keys():
        
        state_scores.update({key : 0})
    
    tweet_scores = {} # initialize empty dictionary
        
    for line in sent_file:  # fill in terms and theirrespective scores
    
        term, score = line.split('\t') # file is tab-delimited
        
        tweet_scores[term] = int(score) # convert the score to integer type    
         
    for line in tweet_file:
        
        # only choose english tweets within the U.S
        if('lang' in line and json.loads(line)['lang'] == 'en'):
            
            # use 'user' attribute to find location
            if(json.loads(line)['user']['location'] in states.keys()):
                
                tweet = json.loads(line)['text']
                
                happy_score = tweet_sentiment(tweet_scores, tweet)
                
                state_scores[json.loads(line)['user']['location']] += happy_score
                
            elif(json.loads(line)['user']['location'] in states.values()):
                
                tweet = json.loads(line)['text']
                
                happy_score = tweet_sentiment(tweet_scores, tweet)
                
                # return key based on value
                state_scores[list(states.keys())[list(states.values()).index(json.loads(line)['user']['location'])]] += happy_score
            
            # use 'place' attribute to find location
            elif(json.loads(line)['place'] is not None):
                
                if(json.loads(line)['place']['name'] in states.keys()):
                    
                    tweet = json.loads(line)['text']
                    
                    happy_score = tweet_sentiment(tweet_scores, tweet)
                
                    state_scores[json.loads(line)['user']['location']] += happy_score
                    
                elif(json.loads(line)['place']['name'] in states.values()):
                    
                    tweet = json.loads(line)['text']
                    
                    happy_score = tweet_sentiment(tweet_scores, tweet)
                
                    state_scores[list(states.keys())[list(states.values()).index(json.loads(line)['place']['name'])]] += happy_score

                else: 
                    continue
            
            else: 
                continue
        
        else: 
            continue
            
    # return the state key with the highest score value
    print max(state_scores, key = state_scores.get)
    
    #print state_scores

def main():
    # hw()
    
    # lines(sent_file)
    
    # lines(tweet_file) 
    
    sent_file = open(sys.argv[1])
    #sent_file = open('AFINN-111.txt') # use this for local machine   
    
    tweet_file = open(sys.argv[2])
    #tweet_file = open('output1.txt') # use this for local machine
    
    happy_state(sent_file, tweet_file)
    
    sent_file.close()
    
    tweet_file.close() 
           
if __name__ == '__main__':
    main()

