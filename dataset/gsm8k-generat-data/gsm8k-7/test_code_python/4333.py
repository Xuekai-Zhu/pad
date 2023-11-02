def solution():
    num_seasons = 10

    # Calculate the first half of the show (seasons 1-5)
    num_episodes_first_half = 20 * 5

    # Calculate the second half of the show (seasons 6-10)
    num_episodes_second_half = 25 * 5

    # Calculate the total number of episodes
    total_episodes = num_episodes_first_half + num_episodes_second_half
    result = total_episodes
    return result

print(solution())