import unittest
import get_stocks


class TestApp(unittest.TestCase):

  def test_add(self):
    result = get_stocks.add(10, 5)
    self.assertEqual(result, 15)

  def test_divide(self):
    self.assertEqual(get_stocks.divide(10, 5),2)
    #self.assertRaises(ValueError, get_stocks.divide, 10, 0)
    with self.assertRaises(ValueError):
      get_stocks.divide(10, 0)



if __name__ == '__main__':
  unittest.main()