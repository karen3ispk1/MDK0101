Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from main import len_num
import unittest
class TestFunction(unittest.TestCase):
  def test_len_num(self):
    self.assertEqual(len_num(5555),4)

  


