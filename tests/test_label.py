import sys
import os
# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from Label_CoNLL_Format import label_field, process_row, process_csv

import unittest

class TestLabelCoNLLFormat(unittest.TestCase):
    
    def test_label_field(self):
        text = "apple banana"
        expected_output = ["apple B-Product", "banana I-Product"]
        self.assertEqual(label_field(text, "Product"), expected_output)
    
    def test_process_row(self):
        row = ["", "", "", "", "100", "apple banana", "", "New York"]
        expected_output = [
            "apple B-Product", "banana I-Product", 
            "100 B-PRICE",
            "New B-LOC", "York I-LOC", ""
        ]
        self.assertEqual(process_row(row), expected_output)

if __name__ == '__main__':
    unittest.main()
