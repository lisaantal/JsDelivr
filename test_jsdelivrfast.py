# test_jsdelivrfast.py
"""
Tests for JsDelivrFast module.
"""

import unittest
from jsdelivrfast import JsDelivrFast

class TestJsDelivrFast(unittest.TestCase):
    """Test cases for JsDelivrFast class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JsDelivrFast()
        self.assertIsInstance(instance, JsDelivrFast)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JsDelivrFast()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
