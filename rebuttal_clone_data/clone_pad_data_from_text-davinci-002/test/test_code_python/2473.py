def solution():
    total_marbles = 500
    given_away = 80 * 4
    remaining_marbles = total_marbles - given_away
    result = remaining_marbles * 4
    return result

print(solution())