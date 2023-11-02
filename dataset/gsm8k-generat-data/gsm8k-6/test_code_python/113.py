def solution():
    # Calculate the number of marbles Baez loses
    lost_marbles = 0.20 * 25

    # Calculate the number of marbles Baez has left after losing some
    remaining_marbles = 25 - lost_marbles

    # Calculate the number of marbles Baez receives from her friend
    friend_marbles = remaining_marbles * 2

    # Calculate the total number of marbles Baez ends up with
    total_marbles = remaining_marbles + friend_marbles
    
    result = total_marbles
    return result

print(solution())