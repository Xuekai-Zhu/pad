def solution():
    """Abigail thinks she has some lost some money out of her purse. She had $11 in her purse at the start of the day, and she spent $2 in a store. If she now has $3 left, how much money has she lost?"""
    starting_money = 11
    money_spent = 2
    remaining_money = 3
    total_lost = starting_money - (money_spent + remaining_money)
    result = total_lost
    return result

print(solution())