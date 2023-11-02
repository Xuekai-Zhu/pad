def solution():
    starting_marbles = 24  # Brianna started with 24 marbles
    lost_marbles = 4  # She lost 4 marbles through a hole in the bag
    given_away_marbles = 2 * lost_marbles  # She gave away twice as many marbles as she had lost
    dog_ate_marbles = lost_marbles / 2  # Her dog ate half as many marbles as she had lost

    # Calculate the total number of marbles she has remaining
    remaining_marbles = starting_marbles - lost_marbles - given_away_marbles - dog_ate_marbles
    result = remaining_marbles
    return result

print(solution())