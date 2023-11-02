def solution():
    """The show Magic King was on the air for 10 seasons and 20 episodes per season for the first half of seasons and 25 for the second half of the show.  How many total episodes were there?"""
    # Define the number of episodes per season for the first and second half of the show
    episodes_first_half = 20
    episodes_second_half = 25

    # Define the number of seasons for the first and second half of the show
    seasons_first_half = 5
    seasons_second_half = 5

    # Calculate the total number of episodes
    total_episodes = (episodes_first_half * seasons_first_half) + (episodes_second_half * seasons_second_half)

    # Display the total number of episodes
    result = total_episodes
    return result

print(solution())