def solution():
    """A TV show has been going on for 14 years. Out of those 14 years, 8 seasons had 15 episodes, 4 seasons had 20 episodes, and 2 seasons had 12 episodes. What is the average number of episodes per year?"""
    total_episodes = (8 * 15) + (4 * 20) + (2 * 12)
    total_years = 14
    avg_episodes_per_year = total_episodes/total_years
    result = avg_episodes_per_year
    return result

print(solution())