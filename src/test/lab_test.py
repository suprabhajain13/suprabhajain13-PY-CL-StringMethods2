import unittest
from src.main.lab import (
    replace_characters,
    split_string,
    join_strings,
    count_occurrences,
    find_char_index,
    starts_with_substring,
    ends_with_substring
)

class TestStringMethods(unittest.TestCase):

    def test_replace_characters(self):
        self.assertEqual(replace_characters("Hello, Python!", "Python", "World"), "Hello, World!")
        self.assertEqual(replace_characters("Python is awesome", "Python", "Java"), "Java is awesome")
        self.assertEqual(replace_characters("PythonPythonPython", "Python", "Java"), "JavaJavaJava")
        
    def test_split_string(self):
        self.assertEqual(split_string("Hello, Python! How are you?", " "), ["Hello,", "Python!", "How", "are", "you?"])
        self.assertEqual(split_string("This is a test", " "), ["This", "is", "a", "test"])
        self.assertEqual(split_string("One-Two-Three", "-"), ["One", "Two", "Three"])
        
    def test_join_strings(self):
        self.assertEqual(join_strings(["Hello", "Python", "World"], " "), "Hello Python World")
        self.assertEqual(join_strings(["Hello", "Python", "World"], "-"), "Hello-Python-World")
        self.assertEqual(join_strings(["1", "2", "3"], ","), "1,2,3")
        
    def test_count_occurrences(self):
        self.assertEqual(count_occurrences("Hello, Python!", "l"), 2)
        self.assertEqual(count_occurrences("Python is powerful", "o"), 2)
        self.assertEqual(count_occurrences("PythonPythonPython", "Python"), 3)
        
    def test_find_char_index(self):
        self.assertEqual(find_char_index("Hello, Python!", "P"), 7)
        self.assertEqual(find_char_index("Hello, Python!", "y"), 8)
        self.assertEqual(find_char_index("Hello, Python!", "x"), -1)
        
    def test_starts_with_substring(self):
        self.assertTrue(starts_with_substring("Hello, Python!", "Hello"))
        self.assertTrue(starts_with_substring("Hello, Python!", "Hell"))
        self.assertFalse(starts_with_substring("Hello, Python!", "Python"))
        
    def test_ends_with_substring(self):
        self.assertTrue(ends_with_substring("Hello, Python!", "Python!"))
        self.assertTrue(ends_with_substring("Hello, Python!", "thon!"))
        self.assertFalse(ends_with_substring("Hello, Python!", "Hello"))

if __name__ == '__main__':
    unittest.main()
