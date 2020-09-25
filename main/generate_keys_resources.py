import nltk
import json
import os
from nltk.stem.lancaster import LancasterStemmer
import pickle


class GenerateKeysResources:
    stemmer = LancasterStemmer()

    stop_words = []
    intents_json = {}
    ignore_words = ["?", "!", ",", '"', '"', "-"]

    dogs_keywords_list_library = []
    dog_names = []

    def __init__(self):
        self.readTheStopWordsFile()
        self.get_the_intents()
        self.main()

    def readTheStopWordsFile(self):
        stopwords_file_lines = open(os.getcwd()[:-4] + "/resources/stopwords").readlines()
        for line in stopwords_file_lines:
            self.stop_words.append(line.strip())

    def get_the_intents(self):
        intent_file = open(os.getcwd()[:-4] + "/resources/keys.json").read()
        self.intents_json = json.loads(intent_file)

    def main(self):
        dog_info_dict_list = []
        for key in self.intents_json['keys']:
            dog_name = key['dog'].title()
            # self.dog_names.append(dog_name)

            key_words = key['keywords']
            dog_key_words_list = []

            for key_word in key_words:
                words_in_keyword = nltk.word_tokenize(key_word)
                dog_key_words_list.extend(words_in_keyword)

            # remove duplicate items from the list
            dog_key_words_list = list(set(dog_key_words_list))

            filtered_words_list = []
            for word in dog_key_words_list:
                if word not in self.stop_words and word not in self.ignore_words:
                    filtered_words_list.append(self.stemmer.stem(word.lower()))

            dog_key_words_list = filtered_words_list
            # self.dogs_keywords_list_library.append(dog_key_words_list)

            dict_elem = {
                "dog": dog_name,
                "key_words": dog_key_words_list
            }

            dog_info_dict_list.append(dict_elem)

        path = os.getcwd()[:-4] + "resources/generated"

        with open(path + "\keys.pkl", 'wb') as f:
            pickle.dump(dog_info_dict_list, f)

        print("Resources generated.")


GenerateKeysResources()
