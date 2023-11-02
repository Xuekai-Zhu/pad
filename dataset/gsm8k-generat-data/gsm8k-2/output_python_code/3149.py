def solution():
    """Percy wants to save up for a new PlayStation, which costs $500. He gets $200 on his birthday and $150 at Christmas. To make the rest of the money, he's going to sell his old PlayStation games for $7.5 each. How many games does he need to sell to reach his goal?"""
    total_cost = 500
    birthday_money = 200
    christmas_money = 150
    amount_left = total_cost - birthday_money - christmas_money
    games_needed = int(amount_left / 7.5)
    result = games_needed
    return result

print(solution())