def solution():
    """Baez has 25 marbles. She loses 20% of them one day. Then a friend sees her and gives her double the amount that Baez has after she lost them. How many marbles does Baez end up with?"""
    # Define the initial number of marbles Baez has
    initial_marbles = 25

    # Calculate the number of marbles Baez loses
    marbles_lost = initial_marbles * 0.2

    # Calculate the number of marbles Baez has after losing some
    marbles_left = initial_marbles - marbles_lost

    # Calculate the number of marbles Baez receives from her friend
    friend_marbles = marbles_left * 2

    # Calculate the total number of marbles Baez ends up with
    total_marbles = marbles_left + friend_marbles

    result = total_marbles
    return result

print(solution())