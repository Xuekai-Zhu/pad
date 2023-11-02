def solution():
    """The show Magic King was on the air for 10 seasons and 20 episodes per season for the first half of seasons and 25 for the second half of the show. How many total episodes were there?"""
    # Define the number of seasons and episodes per season for each half of the show
    seasons = 10
    first_half_episodes = 20
    second_half_episodes = 25

    # Calculate the total number of episodes
    total_episodes = (seasons // 2) * (first_half_episodes + second_half_episodes) + \
                     (seasons % 2) * first_half_episodes

    # return the result
    result = total_episodes
    return result

print(solution())