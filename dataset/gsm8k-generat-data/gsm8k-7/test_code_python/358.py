def solution():
    original_marbles = 0
    lost_marbles = 0.5 * 12
    remaining_marbles = 12 - lost_marbles
    total_marbles = remaining_marbles + 10 + 25
    result = original_marbles + total_marbles
    return result

print(solution())