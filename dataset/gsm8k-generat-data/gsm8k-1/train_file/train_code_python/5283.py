def solution():
    """Kelly has 8 chickens that lay 3 eggs each per day. If Kelly sells these eggs for $5 a dozen. How much money will she make in 4 weeks if she sells all her eggs?"""
    chickens = 8
    eggs_per_chicken = 3
    eggs_per_day = chickens * eggs_per_chicken
    dozen_per_day = eggs_per_day / 12
    price_per_dozen = 5
    dozens_per_week = dozen_per_day * 7
    total_dozens = dozens_per_week * 4
    money_made = total_dozens * price_per_dozen
    result = money_made
    return result

print(solution())