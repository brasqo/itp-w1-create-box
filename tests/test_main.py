import unittest

from create_box import create_box
from create_box import empty_box

first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()

fourth_box_expected = "Height is less than 1"

fifth_box_expected = "Width is less than 1"

sixth_box_expected = "Character is not a string"

seventh_box_expected = '''
****
*  *
****
'''.lstrip()


class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_box_expected)

    # Add your own test using third_box_expected
    def test_large_box(self):
        self.assertEqual(create_box(3, 24, 'x'), third_box_expected)
        
    def test_zero_height(self):
        self.assertEqual(create_box(0, 4, 'x'), fourth_box_expected)
        
    def test_zero_width(self):
        self.assertEqual(create_box(3, 0, '$'), fifth_box_expected)
        
    def test_bad_character(self):
        self.assertEqual(create_box(3, 4, 3), sixth_box_expected)
    
    def test_empty_box(self):
        self.assertEqual(empty_box(3, 4, '*'), seventh_box_expected)
    
    def test_zero_height_empty_box(self):
        self.assertEqual(empty_box(0, 4, 'x'), fourth_box_expected)
        
    def test_zero_width_empty_box(self):
        self.assertEqual(empty_box(3, 0, '$'), fifth_box_expected)
        
    def test_bad_character_empty_box(self):
        self.assertEqual(empty_box(3, 4, 3), sixth_box_expected)
