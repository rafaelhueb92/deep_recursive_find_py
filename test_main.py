import unittest
from main import deep_recursive_find_map

class TestDeepRecursiveFindMap(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(deep_recursive_find_map(5, [1, 2, 3, 5]), [3])
        self.assertEqual(deep_recursive_find_map("x", {"a": "x"}), ["a"])

    def test_nested(self):
        structure = {"a": [{"b": {"c": [0, {"d": 999}, 2]}}]}
        self.assertEqual(deep_recursive_find_map(999, structure), ["a", 0, "b", "c", 1, "d"])

    def test_boolean_and_none(self):
        structure = [True, [False, [None, {"deep": [0, 1, True]}]]]
        self.assertEqual(deep_recursive_find_map(True, structure), [0])
        self.assertEqual(deep_recursive_find_map(False, structure), [1, 0])
        self.assertEqual(deep_recursive_find_map(None, structure), [1, 1, 0])

    def test_mixed_lists_dicts(self):
        structure = {"x": [0, {"y": [1, {"z": 42}]}]}
        self.assertEqual(deep_recursive_find_map(42, structure), ["x", 1, "y", 1, "z"])

if __name__ == "__main__":
    unittest.main()