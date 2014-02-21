'''
#==============================================================================
semantic_parse.py
Created on Feb 13, 2014
@author: aelshen
#==============================================================================
'''
from __future__ import print_function
import os
import sys
import nltk
#==============================================================================
#--------------------------------Constants-------------------------------------
#==============================================================================
DEBUG = False

#==============================================================================
#-----------------------------------Main---------------------------------------
#==============================================================================
def main():
    if len(sys.argv) < 4:
        print("feature_parse.py requires 3 arguments" 
               + os.linesep + "(1)grammar file"
               + os.linesep + "(2)data file"
               + os.linesep + "(3)result file")
        sys.exit()
    
    grammar_file = "file:" + sys.argv[1]
    
    grammar = nltk.data.load(grammar_file)
    data_file = open(sys.argv[2], 'r')
    result_file = open(sys.argv[3], 'w')
    
    #build parser
    parser = nltk.parse.FeatureChartParser(grammar)
    
    #read through all the lines in the data file
    for sentence in data_file.readlines():
        if not sentence.strip():
            continue
        #tokenize the current sentence
        sentence = sentence.strip().split()
        parse = parser.nbest_parse(sentence, 1)
        #if a valid parse was found, print it
        if parse:
            result_file.write(parse[0].node['SEM'].simplify())
            result_file.write(os.linesep)
        #else, print a blank line
        else:
            result_file.write(os.linesep)
    
    print("Hello, World!")

#==============================================================================    
#------------------------------------------------------------------------------
#==============================================================================
if __name__ == "__main__":
    sys.exit( main() )