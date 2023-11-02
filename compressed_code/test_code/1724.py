def solution():
    
    total_episodes = 22
    first_half_episodes = total_episodes // 2
    second_half_episodes = total_episodes - first_half_episodes
    first_half_cost = first_half_episodes * 1000
    second_half_cost = second_half_episodes * 1000 * 2.2
    total_cost = first_half_cost + second_half_cost
    result = total_cost
    return result

print(solution())