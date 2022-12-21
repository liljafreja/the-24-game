from unittest.mock import patch, call

import game_generation


@patch("random.randint", side_effect=[1, 2, 3, 4])
def test_generate_digit_list(randint):
    result = game_generation.generate_digit_list()
    assert result == [1, 2, 3, 4]
    randint.assert_has_calls([call(1, 9), call(1, 9), call(1, 9), call(1, 9)])


def test_create_digits_string():
    digit_list = [2, 4, 2, 4]
    digits_string = game_generation.create_digits_string(digit_list)
    assert digits_string == "2 4 2 4"


@patch("game_generation.create_digits_string", return_value="2 4 2 4")
@patch("builtins.print")
def test_display_digits(print_mock, create_digits_string):
    digit_list = [2, 4, 2, 4]
    game_generation.display_digits(create_digits_string(digit_list))
    print_mock.assert_called_once_with("solve: 2 4 2 4")
