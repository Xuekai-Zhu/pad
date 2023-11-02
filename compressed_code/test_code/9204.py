def solution():
    
    seasons = 10
    first_half_episodes = 20
    second_half_episodes = 25
    total_episodes = (first_half_episodes * (seasons // 2)) + (second_half_episodes * (seasons // 2))
    result = total_episodes
    return result

print(solution())