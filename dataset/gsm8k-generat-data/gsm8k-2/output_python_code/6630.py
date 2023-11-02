def solution():
    """The government gives the bottom 20% of people a $2000 stimulus. They have found that this kind of stimulus returns 5 times as much money to the government, in terms of tax revenue, as it cost. The city has 1000 people in it. What was the government profit from this project?"""
    city_size = 1000
    bottom_20_percent = int(city_size * 0.2)
    stimulus_cost = bottom_20_percent * 2000
    stimulus_return = stimulus_cost * 5
    government_profit = stimulus_return - stimulus_cost
    result = government_profit
    return result

print(solution())