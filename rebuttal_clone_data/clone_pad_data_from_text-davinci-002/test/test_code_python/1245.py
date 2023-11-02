def solution():
    episodes = 22
    initial_cost = 1000
    percent_increase = 120
    increase_amount = initial_cost * (percent_increase / 100)
    second_half_cost = initial_cost + increase_amount
    cost_per_episode = [initial_cost] * (episodes // 2) + [second_half_cost] * (episodes // 2)
    total_cost = sum(cost_per_episode)
    result = total_cost
    
    return result

print(solution())