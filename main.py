# Импортируем классы и функции
from basic_word import BasicWord
from player import Player
from utils import load_random_word

# Старт программы
if __name__ == '__main__':

    # Объявляем переменные
    word_to_stop = ["stop", "стоп"]
    shortest_amount = 3

    # Приветствие, прием имени игрока, создание экземпляров классов
    user_name = input("Введите имя игрока: ")
    print(f"Привет {user_name}!")
    word_to_play = load_random_word(BasicWord)
    player = Player(user_name)
    print(f"Составьте {word_to_play.words_count()} слов из слова {word_to_play.word.upper()}")
    print(f"Слово должно быть не короче {shortest_amount} букв")
    print(f"Чтобы закончить игру, угадайте все слова или напишите {'/'.join(word_to_stop)}")

    # Цикл по приему ответа, проверки ответа, записи ответа
    while word_to_play.words_count() != player.used_words_count():
        user_answer = input("Ответ: ")
        if len(user_answer) < shortest_amount:
            print("Cлишком короткое слово")
        elif user_answer in word_to_stop:
            print(f"Игра завершена, вы угадали {player.used_words_count()} слов!")
            quit()
        elif player.was_used_word(user_answer):
            print("Уже использовано")
        elif not word_to_play.is_allowed_word(user_answer):
            print("Неверно")
        elif word_to_play.is_allowed_word(user_answer):
            player.add_word_to_used(user_answer)
            print("Верно!")

    # Вывод итоговых результатов
    print(f"Игра завершена, вы угадали {player.used_words_count()} слов!")
