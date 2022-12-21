from unittest.mock import patch, call

import main


@patch('builtins.input', return_value=' (7 - (8 / 8)) * 4 ')
@patch('main.generate_digit_list', return_value=[7, 8, 8, 4])
@patch('builtins.print')
def test_main_integration_wanted_result(print_mock, input_mock, generate_digit_list_mock):
    main.main()
    print_mock.assert_has_calls(calls=[
        call("Please provide an expression using each digit exactly once."),
        call("yes, this is indeed 24. :-)")
    ])


@patch('builtins.input', return_value=' (7 - (8 / 8) * 4 ')
@patch('main.generate_digit_list', return_value=[7, 8, 8, 4])
@patch('builtins.print')
def test_main_integration_invalid_expression(print_mock, input_mock, generate_digit_list_mock):
    main.main()
    print_mock.assert_has_calls(calls=[
        call("Please provide an expression using each digit exactly once."),
        call("sorry, this is not a valid expression!")
    ])


@patch('builtins.input', return_value=' (7 / 8 + 8 * 4) ')
@patch('main.generate_digit_list', return_value=[7, 8, 8, 4])
@patch('builtins.print')
def test_main_integration_unwanted_float_result(print_mock, input_mock, generate_digit_list_mock):
    main.main()
    print_mock.assert_has_calls(calls=[
        call("Please provide an expression using each digit exactly once."),
        call("no, this is 32.875.")
    ])
