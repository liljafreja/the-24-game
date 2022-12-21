import random


def generate_digit_list() -> list[int]:
    return [random.randint(1, 9) for _ in range(4)]


def create_digits_string(digits: list[int]) -> str:
    return " ".join(str(i) for i in digits)


def display_digits(digits: list[int]):
    string_of_digits = create_digits_string(digits)
    print("solve: " + string_of_digits)
