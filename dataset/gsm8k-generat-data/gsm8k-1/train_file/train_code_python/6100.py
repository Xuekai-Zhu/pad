def solution():
    """Cary is saving money to buy a new pair of shoes that cost $120. He has already saved $30. He earns $5 for every lawn he mows. If he mows 3 lawns each weekend, how many more weekends will he have to mow lawns before he can afford to buy the shoes?"""
    cost_of_shoes = 120
    amount_saved = 30
    
    amount_left_to_save = cost_of_shoes - amount_saved
    
    lawns_per_weekend = 3
    earnings_per_lawn = 5
    
    weeks_to_save = amount_left_to_save / (lawns_per_weekend * earnings_per_lawn)
    result = weeks_to_save
    return result

print(solution())