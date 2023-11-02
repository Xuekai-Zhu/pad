def solution():
    """Theodore can craft 10 stone statues and 20 wooden statues every month. A stone statue costs $20 and a wooden statue costs $5. He also pays 10 percent of his total earnings in taxes. How much is his total earning every month?"""
    stone_statues = 10
    wooden_statues = 20
    stone_price = 20
    wooden_price = 5
    total_income = (stone_statues * stone_price) + (wooden_statues * wooden_price)
    taxes = total_income * 0.1
    earnings = total_income - taxes
    result = earnings
    return result

print(solution())