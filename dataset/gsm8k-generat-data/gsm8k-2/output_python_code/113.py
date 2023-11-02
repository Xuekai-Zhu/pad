def solution():
    """Baez has 25 marbles. She loses 20% of them one day. Then a friend sees her and gives her double the amount that Baez has after she lost them. How many marbles does Baez end up with?"""
    starting_marbles = 25
    lost_marbles = starting_marbles * 0.2
    remaining_marbles = starting_marbles - lost_marbles
    friend_gives = remaining_marbles * 2
    total_marbles = remaining_marbles + friend_gives
    result = total_marbles
    return result

print(solution())