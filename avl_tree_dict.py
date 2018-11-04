from abstract_dict import AbstractDict


class Node:
    def __init__(self, key=None, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.right = right
        self.left = left
        self.height = 0

    def _copyFrom(self, node):
        self.key = node.key
        self.value = node.value
        self.right = node.right
        self.left = node.left
        self.height = node.height


class AvlTreeDict(AbstractDict):
    def __init__(self):
        self.tree = Node()
        self.arr = []

    def _get_height(self, node):
        if node.left is None:
            l = 0
        else:
            l = node.left.height
        if node.right is None:
            r = 0
        else:
            r = node.right.height
        return (l, r)

    def _balance_factor(self, node):
        bfactor = self._get_height(node)[1] - self._get_height(node)[0]
        return bfactor

    def _fix_height(self, node):
        r = self._get_height(node)[1]
        l = self._get_height(node)[0]
        if l > r:
            node.height = 1 + l
        else:
            node.height = 1 + r

    def _rotate_right(self, node):
        p = Node()
        p._copyFrom(node)
        q = Node()
        q._copyFrom(p.left)
        p.left = q.right
        q.right = p
        self._fix_height(p)
        self._fix_height(q)
        node._copyFrom(q)

    def _rotate_left(self, node):
        p = Node()
        p._copyFrom(node)
        q = Node()
        q._copyFrom(p.right)
        p.right = q.left
        q.left = p
        self._fix_height(p)
        self._fix_height(q)
        node._copyFrom(q)

    def _balance(self, node):
        self._fix_height(node)
        p = Node()
        p._copyFrom(node)
        if self._balance_factor(p) == 2:
            if self._balance_factor(p.right) < 0:
                self._rotate_right(p.right)
            self._rotate_left(p)
        if self._balance_factor(p) == -2:
            if self._balance_factor(p.left) > 0:
                self._rotate_left(p.left)
            self._rotate_right(p)
        node._copyFrom(p)

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
            self._fix_height(node)
        elif key == node.key:
            node.key = key
            node.value = value
        elif key < node.key:
            if node.left is None:
                node.left = Node(key, value)
                self._fix_height(node.left)
            else:
                self.__setitem__(key, value, node.left)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, value)
                self._fix_height(node.right)
            else:
                self.__setitem__(key, value, node.right)
        self._balance(node)

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
        res_node = self._find_node(key)
        if res_node is not None:
            return res_node.value
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

    def _get_tree(self):
        return self.tree

    def __contains__(self, key):
        return self._find_node(key)

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
        copy = AvlTreeDict()
        arr = self.get_array()
        for item in arr:
            copy[item[0]] = item[1]
        return copy

    def fromkeys(self, iterable, value=None):
        d = AvlTreeDict()
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
