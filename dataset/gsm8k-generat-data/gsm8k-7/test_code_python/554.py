def solution():
    num_likes = 24
    total_population = 60
    play_percentage = 0.5
    group_size = 250

    # Calculate the expected number of individuals that like football in the group
    expected_num_likes = (num_likes/total_population) * group_size

    # Calculate the expected number of individuals that play football in the group
    expected_num_play = expected_num_likes * play_percentage

    result = expected_num_play
    return result

print(solution())