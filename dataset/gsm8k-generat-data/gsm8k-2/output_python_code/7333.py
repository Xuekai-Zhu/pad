def solution():
    """Lorin has 4 black marbles. Jimmy has 22 yellow marbles. Alex had twice as many black marbles as Lorin and one half as many yellow marbles as Jimmy. How many marbles does Alex have?"""
    lorin_black = 4
    jimmy_yellow = 22
    alex_black = 2 * lorin_black
    alex_yellow = jimmy_yellow / 2
    total_marbles = lorin_black + jimmy_yellow + alex_black + alex_yellow
    result = total_marbles
    return result

print(solution())