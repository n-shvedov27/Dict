from abstract_dict import AbstractDict


class BinDict(AbstractDict):
    """
        Класс для реализации словаря на основе массива с бинарным поиском.
    """
    def __init__(self):
        self.dict = []

    def _find_index(self, key):
        """
            значение bool, существует ли такой эелмент в массива
                и индекс, если элемент есть
        """
        length = len(self.dict)
        right = length
        left = -1
        if length == 0:
            return False, length
        while left + 1 != right:
            mid = (right + left) // 2
            if self.dict[mid][0] > key:
                right = mid
            else:
                if self.dict[mid][0] == key:
                    return True, mid
                else:
                    left = mid
            index = right
        return False, right

    def __setitem__(self, key, value):
        ex, index = self._find_index(key)
        if not ex:
            self.dict.insert(index, (key, value))
        else:
            self.dict[index] = (key, value)

    def __getitem__(self, key):
        """
            Функция возвращает слово по ключу.
            Если такого ключа нет, генерируется исключение KeyError.
        """
        ex, index = self._find_index(key)
        if ex:
            return self.dict[index][1]
        raise KeyError(key)

    def __delitem__(self, key):
        """
            Функция удаляет из словаря запись (key, value)
            Если такого ключа нет в словаре, генерируется
                исключение KeyError.
        """
        ex, index = self._find_index(key)
        if ex:
            elem = self.dict[index]
            self.dict.remove(elem)
            return elem
        raise KeyError(key)

    def __contains__(self, key):
        ex, index = self._find_index(key)
        return ex

    def __eq__(self, other):
        flag = True
        for key, value in other.items():
            if key in self:
                if self[key] != other[key]:
                    flag = False
            else:
                flag = False
        return flag

    def __len__(self):
        return len(self.dict)

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        answer = "{"
        for item in self.dict:
            key = item[0]
            value = item[1]
            answer += str(key) + ': ' + value.__repr__() + ', '

        answer = answer[:-2]
        answer += "}"
        return answer

    def clear(self):
        self.dict = []

    def copy(self):
        copy = BinDict()
        for item in self.dict:
            copy.dict.append(item)
        return copy

    def fromkeys(self, iterable, value=None):
        d = BinDict()
        for it in iterable:
            d.__setitem__(it, value)
        return d

    def get(self, key):
        return self.__getitem__(key)

    def items(self):
        return self.dict

    def keys(self):
        keys_arr = []
        for key, value in self.dict:
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
        for pair in self.dict:
            ans.append(pair[1])
        return ans

    def setdefault(self, key, value=None):
        if self.__contains__(key):
            return self.__getitem__(key)
        else:
            self.__setitem__(key, value)

    def update(self, other):
        for key, value in other.items():
            self[key] = value
