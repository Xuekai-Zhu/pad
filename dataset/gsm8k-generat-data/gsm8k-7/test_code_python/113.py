def solution():
    starting_marbles = 25
    lost_marbles = starting_marbles * 0.2  # 20% lost
    remaining_marbles = starting_marbles - lost_marbles
    friend_extra_marbles = remaining_marbles * 2
    total_marbles = remaining_marbles + friend_extra_marbles
    result = total_marbles
    return result

print(solution())