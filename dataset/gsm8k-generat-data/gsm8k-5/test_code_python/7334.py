def solution():
    lorin_black = 4  # Lorin has 4 black marbles
    jimmy_yellow = 22  # Jimmy has 22 yellow marbles
    alex_black = lorin_black * 2  # Alex has twice as many black marbles as Lorin
    alex_yellow = jimmy_yellow / 2  # Alex has half as many yellow marbles as Jimmy

    # Calculate the total number of marbles Alex has
    total_marbles = alex_black + alex_yellow
    result = total_marbles
    return result

print(solution())