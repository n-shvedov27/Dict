from abstract_dict import AbstractDict


class Node:
    def __init__(self, key=None, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.right = right
        self.left = left


class BinTreeDict(AbstractDict):
    def __init__(self):
        self.tree = Node()
        self.arr = []

    def __setitem__(self, key, value, node=None):
        """
            Функция добавления слова в словарь.
            Начинает поиск с корня.
        """
        if node is None:
            node = self.tree
        if node.key is None:
            node.key = key
            node.value = value
        elif key == node.key:
            node.key = key
            node.value = value
        elif key < node.key:
            if node.left is None:
                node.left = Node(key, value)
            else:
                self.__setitem__(key, value, node.left)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, value)
            else:
                self.__setitem__(key, value, node.right)

    def _get_from_node(self, node):
        if node is not None:
            self.arr.append((node.key, node.value))
            self._get_from_node(node.left)
            self._get_from_node(node.right)

    def get_array(self):
        """
            Функция возвращает словарь.
        """
        self.arr = []
        self._get_from_node(self.tree)
        return self.arr

    def _find_word_in_node(self, key, node):
        """
            Функция ищет слово в узле.
            Возвращает слово или None.
        """
        if node is None:
            return None
        if node.key is None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return self._find_word_in_node(key, node.left)
        if key > node.key:
            return self._find_word_in_node(key, node.right)

    def _find_node(self, key):
        """
            Функция поиска записи по ключу возвращает Node
        """
        res = self._find_word_in_node(key, self.tree)
        return res

    def __getitem__(self, key):
        """
            Функция ищет слово по ключу.
            если такого ключа нет, генерируется исключение KeyError,
                иначе возвращается значение.
        """
        if self._find_node(key) is not None:
            return self._find_node(key).value
        raise KeyError(key)

    def _right_most(self, node):
        while node.right is not None:
            node = node.right
        return node.key, node.value

    def _del_tree(self, root, key):
        """
            Функция удаления записи из поддерева
        """
        if root is None:
            return None
        if root.key == key:
            if root.left is None and root.right is None:
                return None
            if root.right is None and root.left is not None:
                temp = root.left
                return temp
            if root.left is None and root.right is not None:
                temp = root.right
                return temp
            root.key, root.value = self._right_most(root.left)
            root.left = self._del_tree(root.left, root.key)
            return root
        if key < root.key:
            root.left = self._del_tree(root.left, key)
            return root
        if key > root.key:
            root.right = self._del_tree(root.right, key)
            return root
        return root

    def __delitem__(self, key):
        """
            Функция удаляет из словаря запись (key, value)
            Если такого ключа нет в словаре, генерируется
                исключение KeyError.
        """
        node_to_del = self._find_node(key)
        if node_to_del is not None:
            self.tree = self._del_tree(self.tree, key)
        else:
            raise KeyError(key)

    def __contains__(self, key):
        return self._find_node(key)

    def get_tree(self):
        return self.tree

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
        self.tree = Node()
        self.arr = []

    def copy(self):
        copy = BinTreeDict()
        arr = self.get_array()
        for item in arr:
            copy[item[0]] = item[1]
        return copy

    def fromkeys(self, iterable, value=None):
        d = BinTreeDict()
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
