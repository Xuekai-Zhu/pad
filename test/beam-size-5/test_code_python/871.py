def solution():
    
    starting_marbles = 52
    friend_marbles = 28
    lost_marbles = starting_marbles / 4
    remaining_marbles = starting_marbles - friend_marbles - lost_marbles
    result = remaining_marbles
    return result

print(solution())