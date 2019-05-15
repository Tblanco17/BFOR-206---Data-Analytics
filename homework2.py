import codecs
import re
import collections
import pandas
import nltk 
from collections import Counter
from nltk import FreqDist
wordDict = Counter()


##Number 2####
##This code I borrowed off of stack overflow, it utilizes collections, regular expressions and nltk to pull the 100 most common words out of the hackers.log text and even tells you how many there are for each.
print("Displaying Number 2")
with open('/home/ligma/scripts/hackers.log') as f:
	part2 = f.read().lower()
words = re.findall(r'\w+', part2)
print (Counter(words).most_common(100))
print("There are the 100 most common words in the hackers.log")
##############################################################

##Number 3a###
##This code is used to search actual chat messages
print("Displaying Number 3")
fname =('/home/ligma/scripts/hackers.log')
word=(">")
k=0

with open(fname, 'r') as f:
	for line in f:
		words = line.split()
		for i in words:
			if(i==word):
				k=k+1
print("Roughly the total amount of actual messages:")
print(k)
####################################################
print("Displaying Number 4 ")
#Number4##
with codecs.open('/home/ligma/scripts/hackers.log', 'r', encoding='cp720') as f:
	for line in f:
		wordDict.update(line.strip().split())

for word, count in wordDict.most_common():
	print(word, count)
##################################################################333

print("Displaying Number 6")
##Number 6##
with open('/home/ligma/scripts/hackers.log') as file:
	for line in file:
		url = re.findall(r'^.*https.*$', line)
		if re.findall (r'^.*https.*$', line):
			print(line)

##Number1###
with open('/home/ligma/scripts/hackers.log') as boy:
	for line in boy:
		if "joined" in line:
			print(line)
