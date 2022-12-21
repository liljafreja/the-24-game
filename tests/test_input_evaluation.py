import pytest

import input_evaluation


def test_tokenize_and_validate_string():
    expression_string = "(7 - (8 / 8)) * 4"
    result = input_evaluation.tokenize_and_validate(expression_string, [7, 8, 8, 4])
    assert result == ['(', '7', '-', '(', '8', '/', '8', ')', ')', '*', '4']


def test_tokenize_and_validate_empty_string():
    expression_string = ""
    with pytest.raises(input_evaluation.InvalidInputException):
        input_evaluation.tokenize_and_validate(expression_string, [1, 2, 3, 4])


def test_are_tokens_valid():
    tokens = ['(', '7', '-', '(', '8', '/', '8', ')', ')', '*', '4']
    digit_list = [8, 4, 7, 8]
    assert input_evaluation.are_tokens_valid(tokens, digit_list)


def test_are_tokens_valid_invalid_digit():
    tokens = ['12', '*', '(', '1', '+', '1', ')']
    digit_list = [1, 2, 1, 1]
    assert not input_evaluation.are_tokens_valid(tokens, digit_list)


def test_are_tokens_valid_invalid_operator():
    tokens = ['(', '1', '+', '1', '+', '1', ')', '!']
    digit_list = [1, 1, 1, 1]
    assert not input_evaluation.are_tokens_valid(tokens, digit_list)


def test_are_tokens_valid_digit_overuse():
    tokens = ['4', '*', '3', '*', '(', '1', '+', '1', ')']
    digit_list = [1, 2, 3, 4]
    assert not input_evaluation.are_tokens_valid(tokens, digit_list)


def test_are_tokens_valid_empty_tokens():
    tokens = []
    digit_list = [1, 2, 3, 4]
    assert not input_evaluation.are_tokens_valid(tokens, digit_list)


def test_are_tokens_valid_lots_of_brackets():
    tokens = ['(', '(', '6', ')', ')', '*', '(', '(', '6', '+', '(', '5', '+', '3', ')', ')', ')']
    digit_list = [6, 6, 5, 3]
    assert input_evaluation.are_tokens_valid(tokens, digit_list)


def test_shunting_yard_algorithm():
    expression_string = "(7 - ( 8 / 8 ) ) * 4"
    digit_list = [8, 4, 7, 8]
    assert input_evaluation.shunting_yard_algorithm(expression_string, digit_list) == ['7', '8', '8', '/', '-', '4',
                                                                                       '*']


def test_shunting_yard_algorithm_mismatching_parenthesis():
    expression_string = "(7 - ( 8 / 8 ) * 4"
    digit_list = [8, 4, 7, 8]
    with pytest.raises(input_evaluation.MismatchingParenthesisException):
        input_evaluation.shunting_yard_algorithm(expression_string, digit_list)


def test_shunting_yard_algorithm_no_parenthesis():
    expression_string = "7 - 8 / 8 * 4"
    digit_list = [8, 4, 7, 8]
    assert input_evaluation.shunting_yard_algorithm(expression_string, digit_list) == ['7', '8', '8', '/', '4', '*',
                                                                                       '-']


def test_evaluate_reverse_polish_notation_four_digits():
    reverse_polish_token_list = ['2', '3', '1', '+', '+', '5', '*']
    assert input_evaluation.evaluate_reverse_polish_notation(reverse_polish_token_list) == 30


def test_evaluate_reverse_polish_notation_five_digits():
    reverse_polish_token_list = ['4', '8', '+', '6', '5', '-', '*', '3', '2', '-', '2', '2', '+', '*', '/']
    assert input_evaluation.evaluate_reverse_polish_notation(reverse_polish_token_list) == 3
