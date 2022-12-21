# 🎲 The 24 Game 

This is a game that tests one's mental arithmetic. The player is provided with four digits and is prompted to input an
arithmetic expression equal to 24. This project was written using python 3.10.

The game should be played while adhering to the following rules:

* each digit from the digit list should only be used as often as it appears,
* please make sure that the parenthesis match each other,
* the arithmetic expression should include only digits and not combinations of joined digits,
* only the following operators/functions are allowed: multiplication, division, addition, subtraction.

## Architecture Description

### Game Generation 

The script `game_generation.py` contains functionalities to create the game state. It is in charge of instantiating four
of the random
digits in the range of one to nine and creating a string out of them, which is afterwards displayed as the problem to
the player.

### Input Evaluation

The script `input_evaluation.py` consists of the two stages in parsing the provided arithmetic expression into an
equation
and its corresponding result.

<ins>The Shunting-Yard Algorithm</ins>  parses the arithmetical expression in infix notation and produces a postfix notation
string in the Reverse Polish Notation (RPN). The implementation is based on the pseudocode
given [here](https://en.wikipedia.org/wiki/Shunting_yard_algorithm).
Before running the algorithm, the validity of the provided tokens is checked (see the set of rules provided above).

Example: `3 + 4 x (2 - 1)` results in `3 4 2 1 - x +`.

Note: our function returns a list of strings in the RPN order.

<ins> Evaluation of the RPN</ins>   produces the result of evaluating the RPN, in integer or float format.
The evaluation of the RPN follows two simple rules:

* if the token is a number, it is added to a stack,
* if it is an operator, process the two numbers on top of the stack.

After processing all tokens only one number is left on the stack, which is the result.

### Main

The script `main.py` executes the game. It is tested with integration tests, covering all three possible cases
of game outputs; the evaluation result being 24 or not and an invalid expression.

## Testing

To run all tests, please first make sure that you have activated a virtual environment and install the requirements by
executing

```
pip install -r dev_requirements.txt
```

Afterwards, running all the tests is done using

```
python -m pytest
```

## ✨ Running

Running the application is done by executing

```
python main.py
```