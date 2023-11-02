def solution():
    """Hannah brought $30 to the county fair. She spent half of it on rides and another $5 on dessert. How much, in dollars, is left?"""
    starting_money = 30
    spent_on_rides = starting_money / 2
    spent_on_dessert = 5
    remaining_money = starting_money - spent_on_rides - spent_on_dessert
    result = remaining_money
    return result

print(solution())