def solution():
    """For football season, Zachary wants to buy a new football, a pair of shorts, and a pair of football shoes. The ball costs $3.75, the shorts cost $2.40, and the shoes cost $11.85. Zachary has $10. How much more money does Zachary need?"""
    football_cost = 3.75
    shorts_cost = 2.40
    shoes_cost = 11.85
    total_cost = football_cost + shorts_cost + shoes_cost
    zachary_money = 10
    remaining_money = total_cost - zachary_money
    result = remaining_money
    return result

print(solution())