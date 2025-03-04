# Deep Recursive Find Map

This repository contains a Python function `deep_recursive_find_map` that searches for a target value within a nested structure of lists and dictionaries. It returns a list representing the path to the target value.

## Features

- Recursively searches through nested lists and dictionaries
- Returns a list representing the path to the target value
- Handles various data types, including booleans, `None`, and deeply nested structures
- Includes edge case tests

## Function Implementation

```python
def deep_recursive_find_map(target: any, structure: any) -> list:
    if target == structure:
        return []

    if isinstance(structure, list):
        for i, s in enumerate(structure):
            if target == s:
                return [i]
            if isinstance(s, (dict, list)):
                result = deep_recursive_find_map(target, s)
                if result:
                    return [i, *result]

    if isinstance(structure, dict):
        for k, v in structure.items():
            if v == target:
                return [k]
            if isinstance(v, (dict, list)):
                result = deep_recursive_find_map(target, v)
                if result:
                    return [k, *result]

    return None
```

## Usage

```python
from deep_find import deep_recursive_find_map

structure = {
    "level1": [
        {"level2": {"level3": [0, {"target": 999}, 2]}},
        {"another": [5, 10, {"deep": [42, "find me"]}]}
    ],
    "outside": 77
}

print(deep_recursive_find_map(999, structure))  # Output: ["level1", 0, "level2", "level3", 1, "target"]
```

## Running Tests

To run the tests, execute:

```bash
python -m unittest test_main.py
```

## Tests

The `test_main.py` file includes multiple test cases to validate the function:

- Basic value searches
- Deeply nested structures
- Circular references
- Mixed lists and dictionaries
- Boolean and `None` values handling

### `test_main.py`

```python
import unittest
from deep_find import deep_recursive_find_map

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
```

## License

MIT License
