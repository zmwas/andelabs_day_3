import re

def words(sentence):
    list_of_words= sentence.split()
    word_count_dictionary ={}


    for word in list_of_words:
        if word in word_count_dictionary:
            word_count_dictionary[word]+=1

        else:
            word_count_dictionary[word] =1
    return word_count_dictionary