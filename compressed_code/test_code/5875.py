def solution():
    
    starting_marbles = 25
    lost_marbles = starting_marbles * 0.2
    remaining_marbles = starting_marbles - lost_marbles
    friend_gives = remaining_marbles * 2
    total_marbles = remaining_marbles + friend_gives
    result = total_marbles
    return result

print(solution())