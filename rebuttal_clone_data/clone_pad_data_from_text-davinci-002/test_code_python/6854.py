def solution():
    seasons_15_episodes = 8
    seasons_20_episodes = 4
    seasons_12_episodes = 2
    total_episodes = (seasons_15_episodes * 15) + (seasons_20_episodes * 20) + (seasons_12_episodes * 12)
    number_of_years = 14
    average_episodes_per_year = total_episodes / number_of_years
    result = average_episodes_per_year
    return result

print(solution())