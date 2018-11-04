import re

find_words = re.compile(r'(\w+)')


class AbstractDict:
    """
        Абстрактный класс для реализации словаря.
    """
    def __init__(self):
        pass

    def add_from_file(self, filename, code_table):
        """
            Функция чтения словаря из файла.
            На вход подаются имя файла и кдовая таблица.
            Построчно считываем данные из файла.
        """
        with open(filename, encoding=code_table, errors='replace') as f:
            for line in f:
                self.add_from_line(line)

    def add_from_line(self, line):
        """
            Функция чтения словаря из строки.
            На вход подаётся строка.
            В строке ищутся все слова и добавляются в массив.
        """
        arr = find_words.findall(line)
        self.add_from_array(arr)

    def add_from_array(self, array):
        """
            Функция чтения словаря из массива.
            На вход подаётся массив.
            Первое слово - ключ, второе- значение.
            Если строковое представление элемента существует,
                то добавляем это слово в словарь.
        """
        if len(array) % 2 == 1:
            array.append(None)
        for i in range(len(array)):
            if array[i] is not None and i % 2 == 0:
                self.__setitem__(array[i], array[i + 1])

    def __setitem__(self, key, value):
        """
            Функция добавления слова в словарь.
            На вход подаётся строка.
            Если такого элемента в списке нет, то он добавляется в конец.
            Если есть элемент с таким ключом, то значение заменяется
        """
        pass

    def get_array(self):
        """ Функция возвращает словарь """
        pass

    def __getitem__(self, key):
        """
            Функция ищет запись с ключом key.
            Если слова в словаре нет, то генерируется исключение KeyError,
                иначе возвращается слово.
        """
        pass

    def __delitem__(self, key):
        """
            Функция удаляет из словаря запись (key, value)
            Если такого ключа нет в словаре, генерируется
                исключение KeyError.
        """
        pass
