import requests as requests
from random import shuffle


def load_random_word(class_name):
    """
    Функция:
    - получает список слов с внешнего ресурса,
    - выберает случайное слово,
    - создает экземпляр класса,
    - возвращает этот экземпляр.
    """

    result = requests.get("https://www.jsonkeeper.com/b/H0RB")
    data = result.json()
    shuffle(data)
    word_to_play = data[0]
    example_to_play = class_name(word_to_play["word"], word_to_play["subwords"])

    return example_to_play
