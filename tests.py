import unittest
from main import *


class PasswordTest(unittest.TestCase):

    def test_if_is_a_num(self):
        self.assertEqual(check_if_is_a_num(123), True)
        self.assertEqual(check_if_is_a_num("1223"), True)
        self.assertEqual(check_if_is_a_num("92137"), True)
        self.assertEqual(check_if_is_a_num("123.1"), False)
        self.assertEqual(check_if_is_a_num("12-3"), False)
        self.assertEqual(check_if_is_a_num("112312345i23"), False)
        self.assertEqual(check_if_is_a_num("xxxx"), False)
        self.assertEqual(check_if_is_a_num("123,2"), False)
        self.assertEqual(check_if_is_a_num(123.5), False)

    def test_for_pairs(self):
        self.assertEqual(check_for_digits_pairs(1122), True)
        self.assertEqual(check_for_digits_pairs("1122"), True)
        self.assertEqual(check_for_digits_pairs("1112332222"), True)
        self.assertEqual(check_for_digits_pairs("11212"), False)
        self.assertEqual(check_for_digits_pairs("382451"), False)
        self.assertEqual(check_for_digits_pairs(131232), False)

    def test_if_not_decrease(self):
        self.assertEqual(checks_if_never_decrease(111233), True)
        self.assertEqual(checks_if_never_decrease(123456789), True)
        self.assertEqual(checks_if_never_decrease(111111111), True)
        self.assertEqual(checks_if_never_decrease(111222221), False)
        self.assertEqual(checks_if_never_decrease(11223344554), False)
        self.assertEqual(checks_if_never_decrease("111233"), True)
        self.assertEqual(checks_if_never_decrease("1112133"), False)

    def test_if_between_372002_809992(self):
        self.assertEqual(check_if_is_between(372002), True)
        self.assertEqual(check_if_is_between(809992), True)
        self.assertEqual(check_if_is_between(809993), False)
        self.assertEqual(check_if_is_between(372001), False)
        self.assertEqual(check_if_is_between(459000), True)
        self.assertEqual(check_if_is_between(298000), False)
        self.assertEqual(check_if_is_between(900000), False)

    def test_password(self):
        self.assertEqual(main_validator(11223344), False)
        self.assertEqual(main_validator(123456789), False)
        self.assertEqual(main_validator(1122334499), False)
        self.assertEqual(main_validator(334455669), False)
        self.assertEqual(main_validator(445566), True)
        self.assertEqual(main_validator(456677), True)
        self.assertEqual(main_validator(445565), False)
        self.assertEqual(main_validator(556677), True)
        self.assertEqual(main_validator(566788), True)
        self.assertEqual(main_validator(444555), True)
        self.assertEqual(main_validator(377887), False)
        self.assertEqual(main_validator(366778), False)
        self.assertEqual(main_validator(45678), False)
        self.assertEqual(main_validator(446779), True)
        self.assertEqual(main_validator(788899), True)
        self.assertEqual(main_validator(888999), False)
        self.assertEqual(main_validator(889999), False)
        self.assertEqual(main_validator(778899), True)


if __name__ == "__main__":
    unittest.main()
