def solution():
    initial_marbles = 40
    marbles_lost = 3
    marbles_given = 5
    marbles_received = 12
    total_marbles = initial_marbles + marbles_received - marbles_lost + (marbles_given * 2)
    result = total_marbles
    return result

print(solution())