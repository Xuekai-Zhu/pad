def solution():
    
    original_marbles = 0
    new_marbles = 25
    lost_marbles = 6
    played_marbles = 12 + 10
    remaining_marbles = original_marbles - lost_marbles + played_marbles + new_marbles
    result = remaining_marbles
    return result

print(solution())