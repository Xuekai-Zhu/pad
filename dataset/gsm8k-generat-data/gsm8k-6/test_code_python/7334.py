def solution():
    # Determine how many marbles Alex has
    lorin_black = 4
    alex_black = 2 * lorin_black
    jimmy_yellow = 22
    alex_yellow = 0.5 * jimmy_yellow
    total_marbles = lorin_black + jimmy_yellow + alex_black + alex_yellow
    result = total_marbles
    return result

print(solution())