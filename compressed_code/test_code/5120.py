def solution():
    
    city_size = 1000
    bottom_20_percent = int(city_size * 0.2)
    stimulus_cost = bottom_20_percent * 2000
    stimulus_return = stimulus_cost * 5
    government_profit = stimulus_return - stimulus_cost
    result = government_profit
    return result

print(solution())