from main import deep_recursive_find_map

def test_deep_recursive_find_map():
    # Basic cases
    assert deep_recursive_find_map(3, [1, 2, 3, 4]) == [2]  # Found at index 2
    assert deep_recursive_find_map(5, [1, 2, 3, 4]) is None  # Not found
    assert deep_recursive_find_map("a", ["x", "y", "a", "z"]) == [2]  # Found at index 2
    
    # Nested list cases
    assert deep_recursive_find_map(5, [1, [2, 3, [4, 5]]]) == [1, 2, 1]  # Found in deep nested list
    assert deep_recursive_find_map(6, [1, [2, 3, [4, 5]]]) is None  # Not found

    # Dictionary cases
    assert deep_recursive_find_map(20, {"a": 10, "b": 20, "c": 30}) == ["b"]  # Found at key 'b'
    assert deep_recursive_find_map(40, {"a": 10, "b": 20, "c": 30}) is None  # Not found

    # Nested dictionary cases
    assert deep_recursive_find_map(50, {"a": {"b": {"c": 50}}}) == ["a", "b", "c"]  # Deep nested
    assert deep_recursive_find_map(60, {"a": {"b": {"c": 50}}}) is None  # Not found

    # Mixed list and dictionary cases
    data = [1, {"x": [2, {"y": 99}]}]
    assert deep_recursive_find_map(99, data) == [1, "x", 1, "y"]  # Found deep in mixed structure

    print("All basic tests passed!")

def test_deep_recursive_find_map_edge_cases():
    # Deeply nested structures
    deep_nested_list = [[[[[[[[42]]]]]]]]  # 8 levels deep
    assert deep_recursive_find_map(42, deep_nested_list) == [0, 0, 0, 0, 0, 0, 0,0]  

    deep_nested_dict = {"a": {"b": {"c": {"d": {"e": {"f": {"g": 999}}}}}}}
    assert deep_recursive_find_map(999, deep_nested_dict) == ["a", "b", "c", "d", "e", "f", "g"]  

    # Circular references (Should not crash but will cause infinite recursion)
    a = {}
    a["self"] = a  # Circular reference
    try:
        deep_recursive_find_map(42, a)  
    except RecursionError:
        print("✅ Caught RecursionError for circular reference")

    # Unusual but valid Python objects
    class CustomObject:
        def __init__(self, value):
            self.value = value

    complex_structure = [{"key": [CustomObject(123), {"nested": CustomObject(456)}]}]
    assert deep_recursive_find_map(456, complex_structure) is None  # It won't find objects directly

    print("Edge case tests completed!")

def test_deep_recursive_find_map_advanced():
    # 🏗️ Mixing lists inside dictionaries and vice versa
    complex_structure = {
        "level1": [
            {"level2": {"level3": [0, {"target": 999}, 2]}},
            {"another": [5, 10, {"deep": [42, "find me"]}]}
        ],
        "outside": 77
    }

    assert deep_recursive_find_map(999, complex_structure) == ["level1", 0, "level2", "level3", 1, "target"]
    assert deep_recursive_find_map(42, complex_structure) == ["level1", 1, "another", 2, "deep", 0]
    assert deep_recursive_find_map(77, complex_structure) == ["outside"]
    assert deep_recursive_find_map("find me", complex_structure) == ["level1", 1, "another", 2, "deep", 1]

    # ✅ Booleans and lists inside lists
    bool_list_structure = [
        True,
        [False, [None, {"deep_dict": [0, 1, 2, [3, 4, 5, True]]}]]
    ]

    assert deep_recursive_find_map(True, bool_list_structure) == [0]  # First occurrence
    assert deep_recursive_find_map(False, bool_list_structure) == [1, 0]
    assert deep_recursive_find_map(None, bool_list_structure) == [1, 1, 0]
    assert deep_recursive_find_map(5, bool_list_structure) == [1, 1, 1, "deep_dict", 3, 2]  # Inside a nested list

    print("✅ All advanced tests passed!")


test_deep_recursive_find_map() # Easy
test_deep_recursive_find_map_edge_cases() # Medium
test_deep_recursive_find_map_advanced() # HARD!