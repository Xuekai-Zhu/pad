def solution():
    
    total_marbles = 500
    marbles_given_away = 80 * 4
    remaining_marbles = total_marbles - marbles_given_away
    result = remaining_marbles * 4
    return result

print(solution())