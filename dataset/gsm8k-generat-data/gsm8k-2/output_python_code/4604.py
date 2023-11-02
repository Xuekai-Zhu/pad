def solution():
    """Jane runs a small farm. She has 10 chickens that lay 6 eggs each per week. She can sell the eggs for $2/dozen. How much money will she make in 2 weeks if she sells all her eggs?"""
    chickens = 10
    eggs_per_chicken_per_week = 6
    total_eggs_per_week = chickens * eggs_per_chicken_per_week
    dozens_per_week = total_eggs_per_week / 12
    price_per_dozen = 2
    total_money_per_week = dozens_per_week * price_per_dozen
    total_money = total_money_per_week * 2
    result = total_money
    return result

print(solution())