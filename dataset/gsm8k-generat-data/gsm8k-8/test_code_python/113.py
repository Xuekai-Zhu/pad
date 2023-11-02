def solution():
    # Calculate the number of marbles Baez loses
    lost_marbles = 0.2 * 25

    # Calculate the number of marbles Baez has left
    remaining_marbles = 25 - lost_marbles

    # Calculate the number of marbles her friend gives her
    friend_marbles = 2 * remaining_marbles

    # Calculate the total number of marbles Baez ends up with
    total_marbles = remaining_marbles + friend_marbles
    result = total_marbles
    return result

print(solution())