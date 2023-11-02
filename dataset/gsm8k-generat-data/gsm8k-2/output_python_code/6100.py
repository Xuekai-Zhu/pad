def solution():
    """Cary is saving money to buy a new pair of shoes that cost $120. He has already saved $30. He earns $5 for every lawn he mows. If he mows 3 lawns each weekend, how many more weekends will he have to mow lawns before he can afford to buy the shoes?"""
    cost_of_shoes = 120
    current_savings = 30
    earnings_per_weekend = 15  # 3 lawns mowed * $5 per lawn
    weeks_needed = (cost_of_shoes - current_savings) / earnings_per_weekend
    result = weeks_needed
    return result

print(solution())