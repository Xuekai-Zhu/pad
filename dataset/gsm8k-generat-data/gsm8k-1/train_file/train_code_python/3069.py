def solution():
    """Brianna started out with a bag of 24 marbles. She lost four marbles through a hole in the bag. Then, she gave away twice as many marbles as she had lost through the hole in the bag. Finally, her dog ate half as many marbles as Brianna had lost through the hole in the bag. How many marbles did Brianna have remaining?"""

    initial_marbles = 24
    lost_marbles = 4
    given_away_marbles = 2 * lost_marbles
    dog_ate_marbles = lost_marbles / 2

    remaining_marbles = initial_marbles - lost_marbles - given_away_marbles - dog_ate_marbles

    result = remaining_marbles
    return result

print(solution())