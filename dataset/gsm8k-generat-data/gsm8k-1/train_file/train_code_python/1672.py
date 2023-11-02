def solution():
    """For football season, Zachary wants to buy a new football, a pair of shorts, and a pair of football shoes. The ball costs $3.75, the shorts cost $2.40, and the shoes cost $11.85. Zachary has $10. How much more money does Zachary need?"""
    total_cost = 3.75 + 2.4 + 11.85
    money_available = 10
    money_needed = total_cost - money_available
    result = money_needed
    return result

print(solution())