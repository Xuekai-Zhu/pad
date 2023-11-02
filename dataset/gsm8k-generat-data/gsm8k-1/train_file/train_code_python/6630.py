def solution():
    """The government gives the bottom 20% of people a $2000 stimulus. They have found that this kind of stimulus returns 5 times as much money to the government, in terms of tax revenue, as it cost. The city has 1000 people in it. What was the government profit from this project?"""
    city_population = 1000
    bottom_20_percent = int(city_population * 0.2)
    stimulus_amount = 2000
    stimulus_cost = bottom_20_percent * stimulus_amount
    revenue_generated = stimulus_cost * 5
    government_profit = revenue_generated - stimulus_cost
    result = government_profit
    return result

print(solution())