from typing import Callable, Tuple
from math import sqrt


def index_replacer(n:int, test:Callable[[int],bool], value: str) -> str:
    return value if test(n) else ''

def rule_manager(n:int, rules:list[Tuple[Callable[[int],bool], str]]):
    ret = ''
    for test, val in rules:
        ret += index_replacer(n, test, val)
    return ret or n


FIZZ_BUZZ_RULES = [
    (lambda n: n % 3 == 0, "Fizz" ),
    (lambda n: n % 5 == 0, "Buzz" )
]

JEDI_RULES = [
    *FIZZ_BUZZ_RULES,
    (lambda n: sqrt(n) % 2 == 0, "Meh" ),

]

if __name__ == "__main__":
    print([rule_manager(n, FIZZ_BUZZ_RULES) for n in range(1,51)])
    print("===============")
    print([rule_manager(n, JEDI_RULES) for n in range(1,51)])