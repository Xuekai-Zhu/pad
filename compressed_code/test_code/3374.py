def solution():
    
    first_half_seasons = 5
    second_half_seasons = 5
    first_half_episodes = 20
    second_half_episodes = 25
    total_episodes = (first_half_seasons * first_half_episodes) + (second_half_seasons * second_half_episodes)
    result = total_episodes
    return result

print(solution())