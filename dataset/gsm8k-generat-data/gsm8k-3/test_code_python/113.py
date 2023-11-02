def solution():
    """Baez has 25 marbles. She loses 20% of them one day. Then a friend sees her and gives her double the amount that Baez has after she lost them. How many marbles does Baez end up with?"""
    # Define the initial number of marbles
    initial_marbles = 25

    # Calculate the number of marbles Baez lost
    lost_marbles = initial_marbles * 0.2

    # Calculate the number of marbles Baez has left
    remaining_marbles = initial_marbles - lost_marbles

    # Calculate the number of marbles Baez's friend gives her
    friend_marbles = remaining_marbles * 2

    # Calculate the total number of marbles Baez ends up with
    total_marbles = remaining_marbles + friend_marbles

    # return the result
    result = total_marbles
    return result

print(solution())