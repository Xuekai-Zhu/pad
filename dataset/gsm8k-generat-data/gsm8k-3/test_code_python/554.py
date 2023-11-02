def solution():
    """If 24 out of every 60 individuals like football and out of those that like it, 50% play it, how many people would you expect play football out of a group of 250?"""
    # Determine the proportion of people who like football
    proportion_like = 24/60

    # Determine the proportion of people who both like and play football
    proportion_play = proportion_like * 0.5

    # Determine the expected number of people who play football out of a group of 250
    expected_play = proportion_play * 250

    # Display the expected number of people who play football
    result = expected_play
    return result

print(solution())