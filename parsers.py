################################################################################
# PART #1
# https://stackoverflow.com/questions/21107505/word-count-from-a-txt-file-program
################################################################################
   
    # This function should count the words in an unstructured text document
    # Inputs: A file name (string)
    # Outputs: A dictionary with the counts for each word
    # +1 bonus point for removing punctuation from the wordcounts
    
import string

def countWordsUnstructured(filename):
    wordCounts = {}
    file = open(filename).read().split()
    for word in file:
        for mark in string.punctuation:
            word = word.replace(mark, "")
        if word not in wordCounts:
            wordCounts[word] = 1
        else:
            wordCounts[word] += 1
    return wordCounts

# Prof Danielle's solution    
#def countWordsUnstructured(filename):
    #initialize a word count dictionary
#    wordCounts = {}
    #open a file and read it
#    datafile = open(filename).read()
    #open the file and read it
#    data = datafile.split()
    #count the words
#    for word in data:
#        if word in wordCounts:
#            wordCounts[word] = wordCounts[word] + 1
#        else:
#            wordCounts[word] = 1    
    #return the word count dictionary
#    return wordCounts

# Test your part 1 code below.

#bush1989 = countWordsUnstructured("state-of-the-union-corpus-1989-2017/Bush_1989.txt")
#print (bush1989)

################################################################################
# PART 2
# https://stackoverflow.com/questions/3086973/how-do-i-convert-this-list-of-dictionaries-to-a-csv-file
# https://stackabuse.com/reading-and-writing-csv-files-in-python/
# collab with Marissa and Taylor
################################################################################
    # This function should transform a dictionary containing word counts to a
    # CSV file. The first row of the CSV should be a header noting: 
    # Word, Count
    # Inputs: A word count list and a name for the target file
    # Outputs: A new CSV file named targetfile containing the wordcount data

import csv 

def generateSimpleCSV(targetfile, wordCounts): 
    
    #open a file as a csv_file
    with open(targetfile, "w") as csv_file:
                
        #create the csv
        writer = csv.writer(csv_file)
        
        #make the header row
        writer.writerow(['Word', 'Count'])
        
        #transform the word count dictionary to the content of the csv
        for key,value in wordCounts.items():
            writer.writerow([key, value])
            
    #close file
    csv_file.close()
        
    #return the CSV file
    return csv_file
# 
    
# Test your part 2 code below

#generateSimpleCSV('didthiswork', countWordsUnstructured("state-of-the-union-corpus-1989-2017/Bush_1989.txt"))

################################################################################
# PART 3
# https://www.tutorialspoint.com/python/os_listdir.htm
################################################################################
    # This function should create a dictionary of word count dictionaries
    # The dictionary should have one dictionary per file in the directory
    # Each entry in the dictionary should be a word count dictionary
    # Inputs: A directory containing a set of text files
    # Outputs: A dictionary containing a word count dictionary for each
    #          text file in the directory
    
import os
from os import listdir
    
def countWordsMany(directory): 
    
    #open directory and pull the list of file names
    #path = ('/Users/hannahweber/Dropbox/problem-set-6-hannahweber/state-of-the-union-corpus-1989-2017')
    #path = ('state-of-the-union-corpus-1989-2017')
    directory_list = os.listdir(directory)
    
    #create an empty dictionary for the big dictionary of word count dictionaries
    wordCountDict = {}
        
    #iterate through the entries and create the dictionary containing the other word count dictionaries for each text file entry
    #loop through the list of files
            #for each file, call wordCounts function above for each file
    
    for file in directory_list:
        eachWordCount = countWordsUnstructured(file)
    
        #place the word count dictionary into the empty dictionary
        wordCountDict[file] += eachWordCount

    #return the big dictionary
    return wordCountDict
    
# Test your part 3 code below

big_dictionary = countWordsMany("state-of-the-union-corpus-1989-2017")
print(big_dictionary)

################################################################################
# PART 4
################################################################################
#def generateDirectoryCSV(wordCounts, targetfile): 
    # This function should create a CSV containing the word counts generated in
    # part 3 with the header: 
    # Filename, Word, Count
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: A CSV file named targetfile containing the word count data
    
# Test your part 4 code below
    
################################################################################
# PART 5
################################################################################
#def generateJSONFile(wordCounts, targetfile): 
    # This function should create an containing the word counts generated in
    # part 3. Architect your JSON file such that the hierarchy will allow
    # the user to quickly navigate and compare word counts between files. 
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: An JSON file named targetfile containing the word count data
    
# Test your part 5 code below

################################################################################
# PART 6
################################################################################
#def searchCSV(csvfile, word): 
    # This function should search a CSV file from part 4 and find the filename
    # with the largest count of a specified word
    # Inputs: A CSV file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    
#def searchJSON(JSONfile, word): 
    # This function should search a JSON file from part 5 and find the filename
    # with the largest count of a specified word
    # Inputs: An JSON file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    
# Test your part 6 code to find which file has the highest count of a given word

# +1 bonus point for figuring out how many datapoints you had to process to 
# compute this value

