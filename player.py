class Player:
    """
    Класс `Player`
    **Поля:**
    - имя пользователя,
    - использованные слова пользователя.
    **Методы:**
    - получение количества использованных слов (возвращает int);
    - добавление слова в использованные слова (ничего не возвращает);
    - проверка использования данного слова до этого (возвращает bool).
    """
    def __init__(self, name: str):
        self.name = name
        self.used_words = []

    def used_words_count(self):
        return len(self.used_words)

    def add_word_to_used(self, word_to_add):
        self.used_words.append(word_to_add)

    def was_used_word(self, word_to_check):
        return word_to_check in self.used_words

    def __repr__(self):
        return f"Player('{self.name}', {self.used_words})"
