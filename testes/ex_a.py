import unittest

class soma(unittest.TestCase):
   def test(self):
      a = int(input('Digite um numero: '))
      b = int(input('Digite outro numero: '))
      c = a+b
      self.assertEqual(a + b,c)

if __name__ == '__main__':
   unittest.main()
