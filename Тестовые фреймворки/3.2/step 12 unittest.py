import unittest


class TestAbs(unittest.TestCase):
    # создаем класс, который наследуется от класса TestCase
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    # в последующие методы передаем аргумент self
    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


# assert -> self.assertEqual(required condition, actual condition,message)

if __name__ == "__main__":
    unittest.main()
