from urllib.request import urlopen
import nltk
from abc import ABCMeta, abstractmethod

# OOP


class VictorinaWebDataLoader:
    def __init__(self, filename, tokenizer=None):
        self.tokenizer = tokenizer or 'tokenizers/punkt/english.pickle'
        self.filename = filename

    def load_data(self):
        with open(self.filename) as f:
            return f.read()

    def making_sentences_mass(self):
        data = self.load_data().replace('-\n', '')
        return nltk.data.load(self.tokenizer).tokenize(data.replace('\n', ' '))

# #
# class VictorinaAbstractDataLoader:
#     def __init__(self, tokenizer=None):
#         self.tokenizer = tokenizer or 'tokenizers/punkt/english.pickle'
#
#     @abstractmethod
#     def load_data(self):
#         """
#         :return: text data
#         """
#         raise NotImplemented("please implement me in CHILD classes!!!!")
#
#     def making_sentences_mass(self):
#         return nltk.data.load(self.tokenizer).tokenize(self.load_data().replace('\n', ''))
#
#
# class VictorinaWebDataLoader(VictorinaAbstractDataLoader):
#     def __init__(self, url, tokenizer=None):
#         self.url = url
#         super(VictorinaWebDataLoader, self).__init__(tokenizer)
#
#     def load_data(self):
#         return urlopen(self.url).read()
#
#
# class VictorinaTextDataLoader(VictorinaAbstractDataLoader):
#     def __init__(self, filename, tokenizer=None):
#         self.filename = filename
#         super(VictorinaTextDataLoader, self).__init__(tokenizer)
#
#     def load_data(self):
#         with open(self.filename) as f:
#             raise NotImplemented("Please ipmlement read from a file here!")
#
#             pass
#         pass
#
