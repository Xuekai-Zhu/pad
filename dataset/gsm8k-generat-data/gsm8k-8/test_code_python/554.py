def solution():
    # Calculate the number of individuals who like football
    like_football = 24

    # Calculate the number of individuals who play football out of those who like it
    play_football = 0.5 * like_football

    # Calculate the expected number of people who play football out of a group of 250
    expected_play_football = (play_football / like_football) * 250
    result = expected_play_football
    return result

print(solution())