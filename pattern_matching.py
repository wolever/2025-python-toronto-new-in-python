"""
Strutural pattern matching, similar to many functional languages, was added in Python 3.10.

The tutorial is quite good: https://peps.python.org/pep-0636/

And below are some examples.
"""


import ast
import astpretty


def run_game_command():
    command = input("What are you doing next? ")
    match command.split():
        case ["quit"]:
            print("Goodbye!")
            return
        case ["look"]:
            print("You are in a dark room.")
        case ["get", obj]:
            print(f"You pick up the {obj}.")
        case ["drop", *objects]:
            print(f"You drop: {", ".join(objects)}.")
        case ["go", direction] if direction in ["north", "south", "east", "west"]:
            print(f"You go {direction}.")
        case ["go", _]:
            print("Sorry, you can't go that way")
        case _:
            print(f"Sorry, I couldn't understand {command!r}")
    run_game_command()

run_game_command()


def eval_python_expression(expression: str) -> None:
    """ Evaluates a simple Python math expression: ``1 + 1``, ``2 * 3``, etc.
    """
    parsed = ast.parse(expression)
    astpretty.pprint(parsed)

    def evaluate(node: ast.AST) -> int:
        match node:
            case ast.Expr(value=value):
                return evaluate(value)
            case ast.BinOp(left, op, right):
                left_value = evaluate(left)
                right_value = evaluate(right)
                match op:
                    case ast.Add():
                        return left_value + right_value
                    case ast.Mult():
                        return left_value * right_value
                    case ast.Sub():
                        return left_value - right_value
                    case ast.Div():
                        return left_value / right_value
                    case _:
                        raise ValueError(f"Unknown operator: {op!r}")
            case ast.Constant(value=value):
                return value
            case _:
                raise ValueError(f"Unknown node: {node!r}")

    return evaluate(parsed.body[0])

"""
>>> astpretty.pprint(ast.parse("1 + 1"))
Module(
    body=[
        Expr(
            lineno=1,
            col_offset=0,
            end_lineno=1,
            end_col_offset=5,
            value=BinOp(
                lineno=1,
                col_offset=0,
                end_lineno=1,
                end_col_offset=5,
                left=Constant(lineno=1, col_offset=0, end_lineno=1, end_col_offset=1, value=1, kind=None),
                op=Add(),
                right=Constant(lineno=1, col_offset=4, end_lineno=1, end_col_offset=5, value=1, kind=None),
            ),
        ),
    ],
    type_ignores=[],
)

"""

print(eval_python_expression("1 + 1"))
