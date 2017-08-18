'''
Write a program that accepts a sequence of whitespace separated words
as input and prints the words after removing all duplicate words and
sorting them alphanumerically. Suppose the following input is
supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Your program should take in only one line of input.

You may assume that your program will only be tested
with valid inputs.
'''

sentence = input()


# Define this function to return the expected output
# Do not print it from this function
def singlify(s):
    word_list = s.split()
    word_list_new = []
    words={}

    for word in word_list:
        words[word.lower()]=1
    for word in word_list:
        if words[word.lower()]==1:
            word_list_new.append(word)
            words[word.lower()]=0
    # sort the list
    word_list_new.sort(key=str.lower)

    return ' '.join(word_list_new)
print(singlify(sentence),sep=' ')
