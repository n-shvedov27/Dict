import unittest
from arr_dict import ArrayDict
from bin_dict import BinDict
from bin_tree_dict import BinTreeDict
from avl_tree_dict import AvlTreeDict
from hash_dict import HashDict
from abstract_dict import AbstractDict


class UnitTests(unittest.TestCase):
    # ArrDict
    def test_arr_dict_setitem1(self):
        d = ArrayDict()
        d[1] = 1
        self.assertEquals(d[1], 1)

    def test_arr_dict_setitem2(self):
        d = ArrayDict()
        d[1] = 1
        d[1] = 2
        self.assertEquals(d[1], 2)

    def test_arr_dict_delitem(self):
        d = ArrayDict()
        d[1] = 1
        del d[1]
        self.assertEquals(len(d), 0)

    def test_arr_dict_contains(self):
        d = ArrayDict()
        d[1] = 1
        self.assertEquals(1 in d, True)

    def test_arr_dict_eq1(self):
        d1 = ArrayDict()
        d1[1] = 1
        d2 = ArrayDict()
        d2[1] = 1
        self.assertEquals(d1 == d2, True)

    def test_arr_dict_eq2(self):
        d1 = ArrayDict()
        d1[1] = 1
        d2 = ArrayDict()
        d2[1] = 2
        self.assertEquals(d1 == d2, False)

    def test_arr_dict_ne(self):
        d1 = ArrayDict()
        d1[1] = 1
        d2 = ArrayDict()
        d2[1] = 2
        self.assertEquals(d1 != d2, True)

    def test_arr_dict_repr(self):
        d = ArrayDict()
        d[1] = 1
        self.assertEquals(d.__repr__(), "{1: 1}")

    def test_arr_dict_clear(self):
        d = ArrayDict()
        d[1] = 1
        d.clear()
        self.assertEquals(d.dict, [])

    def test_arr_dict_copy(self):
        d = ArrayDict()
        d[1] = 1
        self.assertEquals(d.copy(), {1: 1})

    def test_arr_dict_fromkeys(self):
        d = ArrayDict()
        self.assertEquals(d.fromkeys([1, 2, 3]), {1: None, 2: None, 3: None})

    def test_arr_dict_get(self):
        d = ArrayDict()
        d[1] = 2
        self.assertEquals(d.get(1), 2)

    def test_arr_dict_items(self):
        d = ArrayDict()
        d[1] = 2
        self.assertEquals(d.items(), [(1, 2)])

    def test_arr_dict_keys(self):
        d = ArrayDict()
        d[1] = 2
        d[2] = 3
        self.assertEquals(d.keys(), [1, 2])

    def test_arr_dict_pop(self):
        d = ArrayDict()
        d[1] = 2
        d.pop(1)
        self.assertEquals(d.dict, [])

    def test_arr_dict_popitem(self):
        d = ArrayDict()
        d[1] = 2
        self.assertEquals(d.popitem(1), (1, 2))

    def test_arr_dict_values(self):
        d = ArrayDict()
        d[1] = 2
        self.assertEquals(d.values(), [2])

    def test_arr_dict_setdefault1(self):
        d = ArrayDict()
        d[1] = 2
        d.setdefault(1, 231)
        self.assertEquals(d[1], 2)

    def test_arr_dict_setdefault2(self):
        d = ArrayDict()
        d.setdefault(1, 231)
        self.assertEquals(d[1], 231)

    def test_arr_dict_update(self):
        d1 = ArrayDict()
        d1[1] = 1
        d2 = ArrayDict()
        d2[2] = 2
        d1.update(d2)
        self.assertEquals(d1, {1: 1, 2: 2})

    # BinDict
    def test_bin_dict_setitem1(self):
        d = BinDict()
        d[1] = 1
        self.assertEquals(d[1], 1)

    def test_bin_dict_setitem2(self):
        d = BinDict()
        d[1] = 1
        d[1] = 2
        self.assertEquals(d[1], 2)

    def test_bin_dict_delitem(self):
        d = BinDict()
        d[1] = 1
        del d[1]
        self.assertEquals(len(d), 0)

    def test_bin_dict_contains(self):
        d = BinDict()
        d[1] = 1
        self.assertEquals(1 in d, True)

    def test_bin_dict_eq1(self):
        d1 = BinDict()
        d1[1] = 1
        d2 = BinDict()
        d2[1] = 1
        self.assertEquals(d1 == d2, True)

    def test_bin_dict_eq2(self):
        d1 = BinDict()
        d1[1] = 1
        d2 = BinDict()
        d2[1] = 2
        self.assertEquals(d1 == d2, False)

    def test_bin_dict_ne(self):
        d1 = BinDict()
        d1[1] = 1
        d2 = BinDict()
        d2[1] = 2
        self.assertEquals(d1 != d2, True)

    def test_bin_dict_repr(self):
        d = BinDict()
        d[1] = 1
        self.assertEquals(d.__repr__(), "{1: 1}")

    def test_bin_dict_clear(self):
        d = BinDict()
        d[1] = 1
        d.clear()
        self.assertEquals(d.dict, [])

    def test_bin_dict_copy(self):
        d = BinDict()
        d[1] = 1
        self.assertEquals(d.copy(), {1: 1})

    def test_bin_dict_fromkeys(self):
        d = BinDict()
        self.assertEquals(d.fromkeys([1, 2, 3]), {1: None, 2: None, 3: None})

    def test_bin_dict_get(self):
        d = BinDict()
        d[1] = 2
        self.assertEquals(d.get(1), 2)

    def test_bin_dict_items(self):
        d = BinDict()
        d[1] = 2
        self.assertEquals(d.items(), [(1, 2)])

    def test_bin_dict_keys(self):
        d = BinDict()
        d[1] = 2
        d[2] = 3
        self.assertEquals(d.keys(), [1, 2])

    def test_bin_dict_pop(self):
        d = BinDict()
        d[1] = 2
        d.pop(1)
        self.assertEquals(d.dict, [])

    def test_bin_dict_popitem(self):
        d = BinDict()
        d[1] = 2
        self.assertEquals(d.popitem(1), (1, 2))

    def test_bin_dict_values(self):
        d = BinDict()
        d[1] = 2
        self.assertEquals(d.values(), [2])

    def test_bin_dict_setdefault1(self):
        d = BinDict()
        d[1] = 2
        d.setdefault(1, 231)
        self.assertEquals(d[1], 2)

    def test_bin_dict_setdefault2(self):
        d = BinDict()
        d.setdefault(1, 231)
        self.assertEquals(d[1], 231)

    def test_bin_dict_update(self):
        d1 = BinDict()
        d1[1] = 1
        d2 = BinDict()
        d2[2] = 2
        d1.update(d2)
        self.assertEquals(d1, {1: 1, 2: 2})

    # BinTreeDict
    def test_bin_tree_dict_setitem1(self):
        d = BinTreeDict()
        d[1] = 1
        self.assertEquals(d[1], 1)

    def test_bin_tree_dict_setitem2(self):
        d = BinTreeDict()
        d[1] = 1
        d[1] = 2
        self.assertEquals(d[1], 2)

    def test_bin_tree_dict_setitem3(self):
        d = BinTreeDict()
        d[2] = 1
        d[1] = 2
        d[10] = 2
        d[9] = 2
        d[8] = 2
        d[7] = 2
        d[5] = 2
        d[12] = 2
        self.assertEquals(d[1], 2)

    def test_bin_tree_dict_delitem(self):
        d = BinTreeDict()
        d[1] = 1
        del d[1]
        self.assertEquals(len(d), 0)

    def test_bin_tree_dict_delitem1(self):
        d = BinTreeDict()
        error = False
        try:
            del d[1]
        except Exception:
            error = True
        self.assertEquals(error, True)

    def test_bin_tree_dict_contains(self):
        d = BinTreeDict()
        d[1] = 1
        self.assertEquals(1 in d, True)

    def test_bin_tree_dict_eq1(self):
        d1 = BinTreeDict()
        d1[1] = 1
        d2 = BinTreeDict()
        d2[1] = 1
        self.assertEquals(d1 == d2, True)

    def test_bin_tree_dict_eq2(self):
        d1 = BinTreeDict()
        d1[1] = 1
        d2 = BinTreeDict()
        d2[1] = 2
        self.assertEquals(d1 == d2, False)

    def test_bin_tree_dict_ne(self):
        d1 = BinTreeDict()
        d1[1] = 1
        d2 = BinTreeDict()
        d2[1] = 2
        self.assertEquals(d1 != d2, True)

    def test_bin_tree_dict_repr(self):
        d = BinTreeDict()
        d[1] = 1
        self.assertEquals(d.__repr__(), "{1: 1}")

    def test_bin_tree_dict_clear(self):
        d = BinTreeDict()
        d[1] = 1
        d[2] = 1
        d.clear()
        self.assertEquals(d, BinTreeDict())

    def test_bin_tree_dict_copy(self):
        d = BinTreeDict()
        d[1] = 1
        self.assertEquals(d.copy(), {1: 1})

    def test_bin_tree_dict_fromkeys(self):
        d = BinTreeDict()
        self.assertEquals(d.fromkeys([1, 2, 3]), {1: None, 2: None, 3: None})

    def test_bin_tree_dict_get(self):
        d = BinTreeDict()
        d[1] = 2
        self.assertEquals(d.get(1), 2)

    def test_bin_tree_dict_items(self):
        d = BinTreeDict()
        d[1] = 2
        self.assertEquals(d.items(), [(1, 2)])

    def test_bin_tree_dict_keys(self):
        d = BinTreeDict()
        d[1] = 2
        d[2] = 3
        self.assertEquals(d.keys(), [1, 2])

    def test_bin_tree_dict_pop(self):
        d = BinTreeDict()
        d[1] = 2
        d.pop(1)
        self.assertEquals(len(d), 0)

    def test_bin_tree_dict_popitem(self):
        d = BinTreeDict()
        d[1] = 2
        self.assertEquals(d.popitem(1), (1, 2))

    def test_bin_tree_dict_values(self):
        d = BinTreeDict()
        d[1] = 2
        self.assertEquals(d.values(), [2])

    def test_bin_tree_dict_setdefault1(self):
        d = BinTreeDict()
        d[1] = 2
        d.setdefault(1, 231)
        self.assertEquals(d[1], 2)

    def test_bin_tree_dict_setdefault2(self):
        d = BinTreeDict()
        d.setdefault(1, 231)
        self.assertEquals(d[1], 231)

    def test_bin_tree_dict_update(self):
        d1 = BinTreeDict()
        d1[1] = 1
        d2 = BinTreeDict()
        d2[2] = 2
        d1.update(d2)
        self.assertEquals(d1, {1: 1, 2: 2})

    # AvlTreeDict
    def test_avl_tree_dict_setitem1(self):
        d = AvlTreeDict()
        d[1] = 1
        self.assertEquals(d[1], 1)

    def test_avl_tree_dict_setitem2(self):
        d = AvlTreeDict()
        d[1] = 1
        d[1] = 2
        self.assertEquals(d[1], 2)

    def test_avl_tree_dict_setitem3(self):
        d = AvlTreeDict()
        d[10] = 1
        d[6] = 1
        d[3] = 1
        d[34] = 1
        d[213] = 1
        d[23] = 1
        d[12] = 2
        self.assertEquals(d[6], 1)

    def test_avl_tree_dict_delitem(self):
        d = AvlTreeDict()
        d[1] = 1
        del d[1]
        self.assertEquals(len(d), 0)

    def test_avl_tree_dict_contains(self):
        d = AvlTreeDict()
        d[1] = 1
        self.assertEquals(1 in d, True)

    def test_avl_tree_dict_eq1(self):
        d1 = AvlTreeDict()
        d1[1] = 1
        d2 = AvlTreeDict()
        d2[1] = 1
        self.assertEquals(d1 == d2, True)

    def test_avl_tree_dict_eq2(self):
        d1 = AvlTreeDict()
        d1[1] = 1
        d2 = AvlTreeDict()
        d2[1] = 2
        self.assertEquals(d1 == d2, False)

    def test_avl_tree_dict_ne(self):
        d1 = AvlTreeDict()
        d1[1] = 1
        d2 = AvlTreeDict()
        d2[1] = 2
        self.assertEquals(d1 != d2, True)

    def test_avl_tree_dict_repr(self):
        d = AvlTreeDict()
        d[1] = 1
        self.assertEquals(d.__repr__(), "{1: 1}")

    def test_avl_tree_dict_clear(self):
        d = AvlTreeDict()
        d[1] = 1
        d[2] = 1
        d.clear()
        self.assertEquals(d, AvlTreeDict())

    def test_avl_tree_dict_copy(self):
        d = AvlTreeDict()
        d[1] = 1
        self.assertEquals(d.copy(), {1: 1})

    def test_avl_tree_dict_fromkeys(self):
        d = AvlTreeDict()
        self.assertEquals(d.fromkeys([1, 2, 3]), {1: None, 2: None, 3: None})

    def test_avl_tree_dict_get(self):
        d = AvlTreeDict()
        d[1] = 2
        self.assertEquals(d.get(1), 2)

    def test_avl_tree_dict_items(self):
        d = AvlTreeDict()
        d[1] = 2
        self.assertEquals(d.items(), [(1, 2)])

    def test_avl_tree_dict_keys(self):
        d = AvlTreeDict()
        d[1] = 2
        d[2] = 3
        self.assertEquals(d.keys(), [1, 2])

    def test_avl_tree_dict_pop(self):
        d = AvlTreeDict()
        d[1] = 2
        d.pop(1)
        self.assertEquals(len(d), 0)

    def test_avl_tree_dict_popitem(self):
        d = AvlTreeDict()
        d[1] = 2
        self.assertEquals(d.popitem(1), (1, 2))

    def test_avl_tree_dict_values(self):
        d = AvlTreeDict()
        d[1] = 2
        self.assertEquals(d.values(), [2])

    def test_avl_tree_dict_setdefault1(self):
        d = AvlTreeDict()
        d[1] = 2
        d.setdefault(1, 231)
        self.assertEquals(d[1], 2)

    def test_avl_tree_dict_setdefault2(self):
        d = AvlTreeDict()
        d.setdefault(1, 231)
        self.assertEquals(d[1], 231)

    def test_avl_tree_dict_update(self):
        d1 = AvlTreeDict()
        d1[1] = 1
        d2 = AvlTreeDict()
        d2[2] = 2
        d1.update(d2)
        self.assertEquals(d1, {1: 1, 2: 2})

    # HashDict
    def test_hash_dict_setitem1(self):
        d = HashDict()
        d[1] = 1
        self.assertEquals(d[1], 1)

    def test_hash_dict_setitem2(self):
        d = HashDict()
        d[1] = 1
        d[1] = 2
        self.assertEquals(d[1], 2)

    def test_hash_dict_delitem(self):
        d = HashDict()
        d[1] = 1
        del d[1]
        self.assertEquals(len(d), 0)

    def test_hash_dict_contains(self):
        d = HashDict()
        d[1] = 1
        self.assertEquals(1 in d, True)

    def test_hash_dict_eq1(self):
        d1 = HashDict()
        d1[1] = 1
        d2 = HashDict()
        d2[1] = 1
        self.assertEquals(d1 == d2, True)

    def test_hash_dict_eq2(self):
        d1 = HashDict()
        d1[1] = 1
        d2 = HashDict()
        d2[1] = 2
        self.assertEquals(d1 == d2, False)

    def test_hash_dict_ne(self):
        d1 = HashDict()
        d1[1] = 1
        d2 = HashDict()
        d2[1] = 2
        self.assertEquals(d1 != d2, True)

    def test_hash_dict_repr(self):
        d = HashDict()
        d[1] = 1
        self.assertEquals(d.__repr__(), "{1: 1}")

    def test_hash_dict_clear(self):
        d = HashDict()
        d[1] = 1
        d[2] = 1
        d.clear()
        self.assertEquals(d, HashDict())

    def test_hash_dict_copy(self):
        d = HashDict()
        d[1] = 2
        self.assertEquals(d.copy(), {1: 2})

    def test_hash_dict_fromkeys(self):
        d = HashDict()
        self.assertEquals(d.fromkeys([1, 2, 3]), {1: None, 2: None, 3: None})

    def test_hash_dict_get(self):
        d = HashDict()
        d[1] = 2
        self.assertEquals(d.get(1), 2)

    def test_hash_dict_items(self):
        d = HashDict()
        d[1] = 2
        self.assertEquals(d.items(), [(1, 2)])

    def test_hash_dict_keys(self):
        d = HashDict()
        d[1] = 2
        d[2] = 3
        self.assertEquals(d.keys(), [1, 2])

    def test_hash_dict_pop(self):
        d = HashDict()
        d[1] = 2
        d.pop(1)
        self.assertEquals(len(d), 0)

    def test_hash_dict_popitem(self):
        d = HashDict()
        d[1] = 2
        self.assertEquals(d.popitem(1), (1, 2))

    def test_hash_dict_values(self):
        d = HashDict()
        d[1] = 2
        self.assertEquals(d.values(), [2])

    def test_hash_dict_setdefault1(self):
        d = HashDict()
        d[1] = 2
        d.setdefault(1, 231)
        self.assertEquals(d[1], 2)

    def test_hash_dict_setdefault2(self):
        d = HashDict()
        d.setdefault(1, 231)
        self.assertEquals(d[1], 231)

    def test_hash_dict_update(self):
        d1 = HashDict()
        d1[1] = 1
        d2 = HashDict()
        d2[2] = 2
        d1.update(d2)
        self.assertEquals(d1, {1: 1, 2: 2})

    def test_abstract_dict_add_from_file(self):
        error = False
        try:
            d = AbstractDict()
            d.add_from_file('for_tests.txt', 'utf-8')
        except Exception:
            error = True
        self.assertEquals(error, False)



if __name__ == '__main__':
    unittest.main()
