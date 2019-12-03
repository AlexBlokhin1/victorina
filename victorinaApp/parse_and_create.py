import random


class VictotinaParseSentences:
    def __init__(self, sentences, words_for_searching, sequence='no_keep_order', min_len=20, max_len=80):
        """

        :param sentences:
        :param words_for_searching:
        :param sequence:
        :param min_len:
        :param max_len:
        """
        # 'no_keep_order', 20, 80
        self.sentences = sentences
        self.words_for_searching = words_for_searching
        self.sequence = sequence
        self.min_len = min_len
        self.max_len = max_len

    # def counting_key_words(self, sentence):
    #     assert isinstance(self.words_for_searching, (list, tuple))
    #     assert isinstance(sentence, (str, tuple))
    #
    #     sentence = sentence.center(len(sentence) + 2)
    #     number_of_key_words = 0
    #
    #     for word in self.words_for_searching:
    #         key_word = word.strip().center(len(word) + 2)
    #
    #         if self.sequence is 'keep_order':
    #             sentence = sentence[sentence.lower().find(key_word.lower())::]
    #
    #         if sentence.lower().find(key_word.lower()) != -1:
    #             number_of_key_words = number_of_key_words + 1
    #             new_sentence = sentence[sentence.lower().find(key_word.lower())::]
    #             # if new_sentence.lower().find(key_word.lower()) != -1:
    #             #     number_of_key_words = 0
    #     return number_of_key_words

    # def check_number_of_key_words(self, sentence):
    #     return self.counting_key_words(sentence) == len(self.words_for_searching)

    def make_question_sentences(self):
        sentences = self.sentences
        question_sentences = []
        answers = []

        for sentence in sentences:
            if self.min_len < len(sentence) < self.max_len:

                for word in self.words_for_searching:
                    key_word = word.strip().center(len(word) + 2)

                    if sentence.lower().find(key_word.lower()) != -1:
                        new_sentence = sentence[sentence.lower().find(key_word.lower())::]
                        if new_sentence.find(key_word.lower()) != -1:

                            sentence = ' '.format() + sentence.lower().replace(key_word,  ' ___ ').capitalize()
                            question_sentences.append(sentence)
                            answers.append(key_word)


                # if self.check_number_of_key_words(sentence):

        return question_sentences, answers

    # def make_question_sentences(self):
    #     question_sentences = []
    #     answers = []
    #     i = 1
    #
    #     sentences_mass = self.finding_sentences()
    #     # random.shuffle(shuffle_mass)
    #
    #     for sentence in sentences_mass:
    #             if sentence[0].isupper():
    #                 index = random.randint(0, len(self.words_for_searching) - 1)
    #                 sentence = ' '.format() + sentence.lower().replace(self.words_for_searching[index], ' ___ ').capitalize()
    #                 question_sentences.append(sentence)
    #                 answers.append(self.words_for_searching[index])
    #                 if i > 10:
    #                     break
    #                 i = i + 1

        # return question_sentences, answers
