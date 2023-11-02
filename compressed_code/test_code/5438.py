def solution():
    
    initial_marbles = 26
    found_marbles = 6
    lost_marbles = 10
    lori_marbles = 2 * lost_marbles
    total_marbles = initial_marbles + found_marbles - lost_marbles + lori_marbles
    result = total_marbles
    return result

print(solution())