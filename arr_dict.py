from abstract_dict import AbstractDict


class ArrayDict(AbstractDict):
    def __init__(self):
        self.dict = []

    def __setitem__(self, key, value):
        for item in self.dict:
            if item[0] == key:
                self.dict.remove(item)
        self.dict.append((key, value))

    def __getitem__(self, key):
        """
            Функция возвращает слово по ключу.
            Если такого ключа нет, генерируется исключение KeyError.
        """
        for elem in self.dict:
            if elem[0] == key:
                return elem[1]
        raise KeyError(key)

    def __delitem__(self, key):
        for elem in self.dict:
            if elem[0] == key:
                self.dict.remove(elem)
                return
        raise KeyError(key)

    def __contains__(self, key):
        flag = False
        for item in self.dict:
            if item[0] == key:
                flag = True
        return flag

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
        copy = ArrayDict()
        for item in self.dict:
            copy.dict.append(item)
        return copy

    def fromkeys(self, iterable, value=None):
        d = ArrayDict()
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
            self.dict.append((key, value))
