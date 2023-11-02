def solution():
    """Ali's class wants to order 35 English textbooks and 35 geography textbooks. Knowing that a geography book costs $10.50 and that an English book costs $7.50, what is the amount of this order?"""
    english_cost = 7.5
    geography_cost = 10.5
    english_quantity = 35
    geography_quantity = 35
    total_cost = (english_cost * english_quantity) + (geography_cost * geography_quantity)
    result = total_cost
    return result

print(solution())