from typing import Union, Tuple
import re


def check_if_is_a_num(password: Union[str, int]) -> bool:
    return str(password).isnumeric()


def check_for_digits_pairs(password: Union[int, str]) -> bool:
    return len(re.findall(r"(.)\1+", str(password))) >= 2


def checks_if_never_decrease(password: Union[int, str]) -> bool:
    password = str(password)
    for i in range(len(password) - 1):
        if password[i] > password[i+1]:
            return False
    return True


def check_if_is_between(password: Union[int, str]):
    return int(password) in range(372002, 809993)


def main_validator(password: Union[int, str]) -> bool:
    return check_if_is_a_num(password) \
           and check_for_digits_pairs(password) \
           and checks_if_never_decrease(password) \
           and check_if_is_between(password)


def password_validator() -> Tuple[int, int]:
    counter = 0
    for i in range(372002, 809993):
        if main_validator(i):
            counter += 1
    return len(range(372002, 809993)), counter


if __name__ == "__main__":
    to_check, valid = password_validator()
    print(f"We checked {to_check} passwords and {valid} of them meets given criteria.")

