def solution():
    """Lorin has 4 black marbles. Jimmy has 22 yellow marbles. Alex had twice as many black marbles as Lorin and one half as many yellow marbles as Jimmy. How many marbles does Alex have?"""
    # Define the number of black marbles Lorin has
    lorin_black = 4

    # Define the number of yellow marbles Jimmy has
    jimmy_yellow = 22

    # Calculate the number of black marbles Alex has
    alex_black = lorin_black * 2

    # Calculate the number of yellow marbles Alex has
    alex_yellow = jimmy_yellow / 2

    # Calculate the total number of marbles Alex has
    total_marbles = alex_black + alex_yellow

    # Display the total number of marbles Alex has
    result = total_marbles
    return result

print(solution())