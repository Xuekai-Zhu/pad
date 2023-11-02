def solution():
    """Baez has 25 marbles. She loses 20% of them one day. Then a friend sees her and gives her double the amount that Baez has after she lost them. How many marbles does Baez end up with?"""
    initial_number_of_marbles = 25
    percent_lost = 20
    number_of_marbles_lost = initial_number_of_marbles * (percent_lost / 100)
    number_of_marbles_after_loss = initial_number_of_marbles - number_of_marbles_lost
    friend_gives_marbles = 2 * number_of_marbles_after_loss
    total_number_of_marbles = number_of_marbles_after_loss + friend_gives_marbles
    result = total_number_of_marbles
    return result

print(solution())