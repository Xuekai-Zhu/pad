def solution():
    """Julie wants to give her favorite cousin a $2345 mountain bike for his birthday. So far, she has saved $1500. Since the birthday is still a few weeks away, Julie has time to save even more. She plans on mowing 20 lawns, delivering 600 newspapers, and walking 24 of her neighbors’ dogs. She is paid $20 for each lawn, 40 cents per newspaper, and $15 per dog. After purchasing the bike, how much money will Julie have left?"""
    bike_price = 2345
    current_savings = 1500
    lawn_income = 20 * 20
    newspaper_income = 0.4 * 600
    dog_income = 15 * 24
    total_income = lawn_income + newspaper_income + dog_income
    total_savings = current_savings + total_income
    money_left = total_savings - bike_price
    result = money_left
    return result

print(solution())