from abstract_dict import AbstractDict


class HashDict(AbstractDict):
    def __init__(self, hash_func=hash, n=997):
        """
            Инициализируем таблицу как массив из 1000 элементов,
                каждый из которых также является массивом, которые
                в прцессе инициализации заполняются значениями None
        """
        self.hash_func = hash_func
        self.hash_table = []
        self.n = n
        for i in range(self.n):
            self.hash_table.append(None)

    def __setitem__(self, key, value):
        """
            Функция добавления слова в словарь.
            На вход подаётся слово.
            Считаем хэш встроенной функцией.
            Индекс в хэш-таблице определяем как остаток от деления
                хэша на размер таблицы.
            По этому индексу добавляем list [(key, value), hash].
        """
        _hash = self.hash_func(key)
        index = abs(_hash) % self.n
        if self.hash_table[index] is None:
            self.hash_table[index] = [[(key, value), _hash]]
            return
        else:
            flag = False
            if len(self.hash_table[index]) > self.n / 2:
                self._update_table()
            for elem in self.hash_table[index]:
                if _hash == elem[1] and key == elem[0][0]:
                    elem[0] = (key, value)
                    flag = True
                    break
            if not flag:
                self.hash_table[index].append([(key, value), _hash])

    def get_array(self):
        arr = []
        for elem in self.hash_table:
            if elem is not None:
                for x in elem:
                    arr.append(x[0])

        return arr

    def __getitem__(self, key):
        """
            Функция ищет слово по ключу.
            если такого ключа нет, генерируется исключение KeyError,
                иначе возвращается значение.
        """
        _hash = self.hash_func(key)
        index = abs(_hash) % self.n
        if self.hash_table[index] is None:
            raise KeyError(key)
        else:
            flag = False
            for elem in self.hash_table[index]:
                if _hash == elem[1] and key == elem[0][0]:
                    return elem[0][1]
            raise KeyError(key)

    def __delitem__(self, key):
        """
            Функция удаляет из словаря запись (key, value)
            Если такого ключа нет в словаре, генерируется
                исключение KeyError.
        """
        _hash = self.hash_func(key)
        index = abs(_hash) % self.n
        if self.hash_table[index] is None:
            raise KeyError(key)
        for elem in self.hash_table[index]:
            if elem is not None and elem[1] == _hash and elem[0][0] == key:
                self.hash_table[index].remove(elem)
                return elem
        raise KeyError(key)

    def _update_table(self):
        """
            Функция перехеширования
        """
        n = self.n
        self.n = self.n * 2
        h_table = []
        for i in range(self.n):
            h_table.append(None)
        for line in self.hash_table:
            if line is not None:
                for elem in line:
                    index = abs(elem[1]) % self.n
                    if h_table[index] is None:
                        h_table[index] = [elem]
                    else:
                        h_table[index].append(elem)
        self.hash_table = h_table

    def _get_hash_table(self):
        return self.hash_table

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        return True

    def __eq__(self, other):
        arr1 = self.get_array()
        arr2 = other.items()
        if len(arr1) != len(arr2):
            return False
        for item in arr1:
            if item not in arr2:
                return False
        for item in arr2:
            if item not in arr1:
                return False
        return True

    def __len__(self):
        return len(self.get_array())

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        arr = self.get_array()
        answer = "{"
        for item in arr:
            key = item[0]
            value = item[1]
            answer += str(key) + ': ' + value.__repr__() + ', '

        answer = answer[:-2]
        answer += "}"
        return answer

    def clear(self):
        self.__init__(hash_func=self.hash_func, n=self.n)

    def copy(self):
        copy = HashDict(hash_func=self.hash_func, n=self.n)
        arr = self.get_array()
        for item in arr:
            copy[item[0]] = item[1]
        return copy

    def fromkeys(self, iterable, value=None):
        d = HashDict()
        for it in iterable:
            d.__setitem__(it, value)
        return d

    def get(self, key):
        return self.__getitem__(key)

    def items(self):
        return self.get_array()

    def keys(self):
        keys_arr = []
        arr = self.get_array()
        for key, value in arr:
            keys_arr.append(key)
        return keys_arr

    def pop(self, key):
        value = self.__getitem__(key)
        self.__delitem__(key)
        return value

    def popitem(self, key):
        pair = (key, self.__getitem__(key))
        self.__delitem__(key)
        return pair

    def values(self):
        ans = []
        arr = self.get_array()
        for pair in arr:
            ans.append(pair[1])
        return ans

    def setdefault(self, key, value=None):
        if self.__contains__(key):
            return self.__getitem__(key)
        else:
            self.__setitem__(key, value)

    def update(self, other):
        for key, value in other.items():
            self.__setitem__(key, value)
