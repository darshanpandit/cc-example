import os
import fileinput
from collections import Counter
from streamprocessors import Streaming_median_calculator

#Emit tweets from text-files in the folder
def fetch_from_text(input_directory):
    #Iterate through each text file in the folder
    for dir_entry in os.listdir(input_directory):
        for line in open( os.path.join(input_directory, dir_entry) , 'r' ):
            yield line

def tokenize(tweet):
    #Seperate function allows to include more complex tokenization schemes for future
    for token in tweet.split():
        if len(token)>0:
            #We assume each word to be a token.
            yield token

def main():
    input_directory = r'tweet_input'
    output_directory = r'tweet_output'

    ft2 = open(os.path.join(output_directory, 'ft2.txt'),'w')

    #To maintain median calculation
    smc = Streaming_median_calculator()


    '''We assume that all the unique words in corpus can fit in Primary Memory
    Complex Postings Lists are distributed and spill to disks when needed.
    They may comprise of one or more datastructures.
    '''
    global_cnt = Counter()

    #Local Postings List for each tweet
    local_cnt  = Counter()

    for line in fetch_from_text(input_directory):
        for token in tokenize(line):
            local_cnt[token] +=1
        global_cnt += local_cnt

        #list(local_cnt) -> generator to calculate unique elements
        #emit unique word-length of the tweet
        ft2.write(str(smc.push(len(list(local_cnt))))+'\n')


        #reset local_cnt to empty
        local_cnt.clear()

    #First Feature
    #If the datastructure gets very large, we can also dump it unsorted into a file on disk and then perform infile sorting.
    posting_list = sorted(dict(global_cnt).items())
    ft1 = open(os.path.join(output_directory, 'ft1.txt'),'w')
    ft1.writelines('{0}\t{1}\n'.format(token,count) for token, count in posting_list )
    ft1.close()

    #Second Feature
    #Values written as they are emitted
    ft2.close()

if __name__ == "__main__":
    main()
