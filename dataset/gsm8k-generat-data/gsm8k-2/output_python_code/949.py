def solution():
    """Theodore can craft 10 stone statues and 20 wooden statues every month. A stone statue costs $20 and a wooden statue costs $5. He also pays 10 percent of his total earnings in taxes. How much is his total earning every month?"""
    stone_statues = 10
    wooden_statues = 20
    stone_cost = 20
    wooden_cost = 5
    total_stone_earnings = stone_statues * stone_cost
    total_wooden_earnings = wooden_statues * wooden_cost
    total_earnings = total_stone_earnings + total_wooden_earnings
    taxes = total_earnings * 0.1
    net_earnings = total_earnings - taxes
    result = net_earnings
    return result

print(solution())