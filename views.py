import os
from django.shortcuts import render
from django.conf import settings
from victorina1.victorinaApp import load_text, parse_and_create, make_json_dictionary
import random


def homepage(request):
    template_name = "victorina/home_page.html"
    return render(request, template_name, context={})


def get_victorina(request):
    book = request.GET.get('book', '')
    template_name = "victorina/index333.html"

    quiz = {
        "test": ['will', 'going to', 'will be', 'shall'],
        "fast": ['going to', 'shall', 'will have', 'must']
    }
    loader = load_text.VictorinaWebDataLoader(os.path.join(settings.VICTORINA_BOOKS_FOLDER,book))
    quiz_data = parse_and_create.VictotinaParseSentences(loader.making_sentences_mass(), quiz['test'], 'no_keep_order', 20, 80)
    start_victorina1 = make_json_dictionary.VictorinaDictionary(quiz_data.make_question_sentences(), quiz['fast'])

    mass1 = start_victorina1.make_dictionary()
    random.shuffle(mass1)

    return render(request, template_name, context={"tests": mass1})

# def get_victorina(request):
#     book = request.GET.get('book', '')
#     template_name = "index333.html"
#
#     loader = load_text.VictorinaWebDataLoader("books/" + book)
#     sentences_and_answers1 = parse_and_create.VictotinaParseSentences(loader.making_sentences_mass(), ['will', 'going to', 'will be', 'shall'], 'no_keep_order', 20, 80)
#     start_victorina1 = make_json_dictionary.VictorinaDictionary(sentences_and_answers1.make_question_sentences(), ['going to', 'shall', 'will have', 'must'])
#
#     mass1 = start_victorina1.make_dictionary()
#     random.shuffle(mass1)
#     #
#     # for i in range(10):
#     #     mass_with_whole_questions = mass1 + mass2 + mass3 + mass4
#     # random.shuffle(mass_with_whole_questions)
#     # mass_with_whole_questions = [mass1, mass2, mass3, mass4]
#
#     return render(request, template_name, context={"tests": mass1})
#
