def solution():
    """If 24 out of every 60 individuals like football and out of those that like it, 50% play it, how many people would you expect play football out of a group of 250?"""
    # Calculate the proportion of individuals that like football
    football_prop = 24 / 60

    # Calculate the proportion of those that like football that play it
    play_football_prop = 0.5

    # Calculate the expected number of people that play football out of a group of 250
    expected_play_football = 250 * football_prop * play_football_prop

    # Round the result to the nearest whole number
    result = round(expected_play_football)
    return result

print(solution())