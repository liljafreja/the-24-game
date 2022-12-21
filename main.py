import input_evaluation
from input_evaluation import InvalidInputException, MismatchingParenthesisException, tokenize_and_validate
from game_generation import generate_digit_list, display_digits


def main():
    digit_list = generate_digit_list()
    display_digits(digit_list)
    print("Please provide an expression using each digit exactly once.")
    expression = input()
    wanted_result = 24
    try:
        tokens = tokenize_and_validate(expression, digit_list)
        reverse_polish_expression = input_evaluation.shunting_yard_algorithm(tokens, digit_list)
        expression_result = input_evaluation.evaluate_reverse_polish_notation(reverse_polish_expression)
        if expression_result != wanted_result:
            print(f"no, this is {expression_result}.")
        else:
            print(f"yes, this is indeed {wanted_result}. :-)")
    except (InvalidInputException, MismatchingParenthesisException):
        print("sorry, this is not a valid expression!")


if __name__ == '__main__':
    main()
