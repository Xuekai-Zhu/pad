def solution():
    initial_marbles = 30
    taken_marbles = initial_marbles * (3/5)
    remaining_marbles = initial_marbles - taken_marbles
    divided_marbles = remaining_marbles / 2
    cleo_marbles = divided_marbles / 2
    result = cleo_marbles
    return result

print(solution())