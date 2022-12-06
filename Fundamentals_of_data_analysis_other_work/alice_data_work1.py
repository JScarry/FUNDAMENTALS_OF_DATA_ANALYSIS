# make HTTP request for internet sources.
#from itertools import pairwise
import urllib.request
# The URL of a text version of Aline in wonderland.
book_url = 'https://www.gutenberg.org/files/11/11-0.txt'

# Get the book -- wrap it in a list to get entire book. otherwise it is fetched line by line.
book = list(urllib.request.urlopen(book_url))

# Decode the lines and strip line endings -- decode book form bytes to unicode.
# So - decode the book line by line, strip the new line /n, and put all the unicode lines into the list.
# In python - this is known as a list comprehension.
book = [line.decode('utf-8-sig').strip() for line in book]

# Get a sample paragraph - Look by hand
# take lines 58 to 62, and join them with a single space, in a single string.
paragraph = ' '.join(book[58:63])

# Show the paragraph
print (paragraph)

# Clean the paragraph up a little.
# Return all in lower case.
alice = paragraph.lower()

# All letters and a space
chars = 'abcdefghijklmnopqrstuvwxyz '

# And strip anything that is not a letter or space.
alice = ''.join([c for c in alice if c in chars])

print()
print()
print(alice)

#Now lets generate a random string of letters 
import random

#print a random characheter
print()
print()
print(random.choice(chars))

#get the length of alice
N = len(alice)

# Generate N random charachters from chars
generated = random.choices(chars, k=N)

# Join them together in a string.
generated = ''.join(generated)

print()
print()
print(generated)

# get the whole book

sbook =''.join(book[26:]).lower()

#cross ref with chars list
weights = [sbook.count(c) for c in chars]

#show weights
weights
print(weights)

#generate a string using those weights
weight_genr = random.choices(chars, weights=weights, k=N)

#join them in a string
weight_genr = ''.join(weight_genr)

# Print
print(weight_genr)
# output is somewhere between English and Random, because we put a constraint on it.

# add the previous charachter as part of the weighting --- avoid the eeee

# create the weights. {Curly brackets for a dictionary}

two_weights = {c:  {d: sbook.count(c + d) for d in chars} for c in chars}
# show the weights
two_weights
print()
print('xxxxxxxxxxxxxxxxxxxxxxxxxxx')
print(two_weights)
print()


# we have to start with some letter
#loop through our char set
for i in range(len(chars)):
    # Print the charachter and how many times it appears in Alice in wonderland
    print(f'{chars[i]}: {weights[i]}') #f strings in python

# start with space
pairs = ' '

# do the following 999 times
for i in range(1,1000):
    # get the weight where previous charachter is the last charachter in twos.
    wt = two_weights[pairs[-1]]
    #turn wt into list ordered by chars
    wt = [wt[c] for c in chars]
    # randomly pick the next charachter using those weights:
    nextc = random.choices(chars, weights=weights, k=1)[0] #note difference between random.choices and random.choices
    # append the charachter to twos.
    pairs = pairs + nextc

print()
print()
print(pairs)



