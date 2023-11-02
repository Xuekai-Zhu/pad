def solution():
    """A TV show has been going on for 14 years. Out of those 14 years, 8 seasons had 15 episodes, 4 seasons had 20 episodes, and 2 seasons had 12 episodes. What is the average number of episodes per year?"""
    # Define the number of years the show has been running
    years = 14

    # Define the number of episodes per season
    eps_15 = 15
    eps_20 = 20
    eps_12 = 12

    # Calculate the total number of episodes
    total_eps = 8 * eps_15 + 4 * eps_20 + 2 * eps_12

    # Calculate the average number of episodes per year
    avg_eps_per_year = total_eps / years

    # Return the result
    result = avg_eps_per_year
    return result

print(solution())