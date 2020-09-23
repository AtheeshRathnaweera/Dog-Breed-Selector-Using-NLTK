import pickle
import os
import nltk

from nltk.stem.lancaster import LancasterStemmer

stop_words = []
ignore_words = ["?", "!", ",", '"', '"', ".", "-"]

stemmer = LancasterStemmer()

keys = pickle.load(open(os.getcwd()[:-4] + "resources/generated" + '\keys.pkl', 'rb'))

for key in keys:
    key["words_amount"] = 0

words_exist_amount = []

# read the stop words
stopwords_file_lines = open(os.getcwd()[:-4] + "/resources/stopwords").readlines()
for line in stopwords_file_lines:
    stop_words.append(line.strip())

main_paragraph = input("Enter the paragraph : ")

sentences = nltk.sent_tokenize(main_paragraph)  # tokenize to list of sentences

for sentence in sentences:
    words = nltk.word_tokenize(sentence)

    for word in words:
        if word not in stop_words and word not in ignore_words:
            stemmed_word = stemmer.stem(word.lower())

            for key_words in keys:
                if stemmed_word in key_words["key_words"]:
                    key_words["words_amount"] = key_words["words_amount"] + 1

highest_count = 0
suggested_dog_names = []
for key in keys:
    words_amount = key["words_amount"]
    if highest_count <= words_amount:
        highest_count = words_amount
        suggested_dog_names.append(key["dog"])

if len(suggested_dog_names) == 0:
    print("Insufficient details for suggest a a dog")
elif len(suggested_dog_names) == 1:
    print("Suggested dog : ", suggested_dog_names[0])
else:
    print("Suggested dogs : ", ', '.join(suggested_dog_names))
