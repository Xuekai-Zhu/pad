def solution():
    """Lorin has 4 black marbles. Jimmy has 22 yellow marbles. Alex had twice as many black marbles as Lorin and one half as many yellow marbles as Jimmy. How many marbles does Alex have?"""
    # Define the number of marbles Lorin and Jimmy have
    lorin_black_marbles = 4
    jimmy_yellow_marbles = 22

    # Calculate the number of marbles Alex has
    alex_black_marbles = 2 * lorin_black_marbles
    alex_yellow_marbles = jimmy_yellow_marbles / 2
    alex_total_marbles = alex_black_marbles + alex_yellow_marbles

    result = alex_total_marbles
    return result

print(solution())