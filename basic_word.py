
class BasicWord:
    """
    Класс `BasicWord`
    **Поля:**
    - исходное слово,
    - набор допустимых подслов.
    **Методы:**
    - проверку введенного слова в списке допустимых подслов (вернет bool),
    - подсчет количества подслов (вернет int).
    **При инициализации** экземпляру задаются:
    **исходное слово** и набор **допустимых слов,** составленных из исходного. ****
    """

    def __init__(self, word: str, allowed_words: list):
        self.word = word
        self.allowed_words = allowed_words

    def is_allowed_word(self, user_answer):
        return user_answer in self.allowed_words

    def words_count(self):
        return len(self.allowed_words)

    def __repr__(self):
        return f"BasicWord('{self.word}', {self.allowed_words})"
