import re
from numbers import Number

PRECEDENCE = {'*': 1, '/': 1, '+': 0, '-': 0}


class InvalidInputException(Exception):
    pass


class MismatchingParenthesisException(Exception):
    pass


def tokenize_and_validate(expression: str, digit_list: list[int]) -> list[str]:
    tokens = re.findall(r" *([+\-*/()]|\d+\.\d+|\d+) *", expression)
    if not are_tokens_valid(tokens, digit_list):
        raise InvalidInputException()
    return tokens


def is_a_bracket(token: str) -> bool:
    return token in ['(', ')']


def are_tokens_valid(tokens: list[str], digits: list[int]) -> bool:
    only_allowed_tokens_present = all(token in PRECEDENCE or
                                      token.isdigit() or
                                      is_a_bracket(token) for token in tokens)
    expected_digits_are_used = sorted(int(digit) for digit in tokens if digit.isdigit()) == sorted(digits)
    return only_allowed_tokens_present and expected_digits_are_used


def is_operator_on_top(operator_stack: list[str]) -> bool:
    return operator_stack and operator_stack[-1] in PRECEDENCE


def has_higher_precedence(token: str, top_operator: str) -> bool:
    return PRECEDENCE[token] <= PRECEDENCE[top_operator]


def shunting_yard_algorithm(tokens: list[str], digits: list[int]) -> list[str]:
    output_queue = []
    operator_stack = []
    for token in tokens:
        if token.isdigit() and int(token) in digits:
            output_queue.append(token)
        if token in PRECEDENCE:
            while is_operator_on_top(operator_stack) and has_higher_precedence(token, operator_stack[-1]):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        if token == '(':
            operator_stack.append(token)
        if token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            if len(operator_stack) == 0:
                raise MismatchingParenthesisException()
            if operator_stack[-1] == '(':
                operator_stack.pop()
    while operator_stack:
        if is_a_bracket(operator_stack[-1]):
            raise MismatchingParenthesisException()
        if operator_stack[-1] != '(':
            output_queue.append(operator_stack.pop())
    return output_queue


def evaluate_reverse_polish_notation(reverse_polish_tokens: list[str]) -> Number:
    stack = []
    for token in reverse_polish_tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            second = stack.pop()
            first = stack.pop()
            match token:
                case '*':
                    stack.append(first * second)
                case '/':
                    stack.append(first / second)
                case '+':
                    stack.append(first + second)
                case '-':
                    stack.append(first - second)
    return stack[-1]
