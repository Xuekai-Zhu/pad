def solution():
    """Hannah brought $30 to the county fair. She spent half of it on rides and another $5 on dessert. How much, in dollars, is left?"""
    initial_money = 30
    money_spent_on_rides = initial_money / 2
    money_left = initial_money - money_spent_on_rides - 5
    result = money_left
    return result

print(solution())