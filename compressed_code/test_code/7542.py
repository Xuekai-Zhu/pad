def solution():
    
    first_half_episodes = 11
    second_half_episodes = 11
    first_half_cost = first_half_episodes * 1000
    second_half_cost = second_half_episodes * 1000 * 2.2
    total_cost = first_half_cost + second_half_cost
    result = total_cost
    
    return result

print(solution())