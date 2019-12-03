import random

example = """
    tests = [
        {"question": "how are you?", "answer1": "OK", "answer2": "SO SO", "answer3": "AMAZING", "answer4": "AWFUL"},
        {"question": "What day is it today?", "answer1": "Thursday", "answer2": "Monday", "answer3": "Wednesday", "answer4": "Friday"},

     ]
"""


class VictorinaDictionary:
    def __init__(self, sentences_and_answers, whole_variants):
        self.sentences_and_key_words = sentences_and_answers
        self.whole_variants = whole_variants

    def make_dictionary(self):
        key_symbol = ' ___ '
        (question_sentences, answers) = self.sentences_and_key_words
        result = []
        for i in range(len(question_sentences) - 1):
            variants_for_question = []

            while True:
                index = random.randint(0, (len(self.whole_variants) - 1))
                new_variant = self.whole_variants[index]

                if new_variant not in variants_for_question:
                    variants_for_question.append(new_variant)

                if len(variants_for_question) == 3:
                    break

            variants_for_question.append(answers[i])
            random.shuffle(variants_for_question)
            result.append(
                {"question": question_sentences[i], "id": i+1, "key_symbol": key_symbol, "variant1": variants_for_question[0], "variant2": variants_for_question[1], "variant3": variants_for_question[2],
                 "variant4": variants_for_question[3], "answer": answers[i]})

            if i == 10:
                break

        return result


