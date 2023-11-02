def solution():
    """Hannah brought $30 to the county fair. She spent half of it on rides and another $5 on dessert. How much, in dollars, is left?"""
    # Define the amount of money Hannah brought to the fair
    money = 30

    # Calculate the amount of money Hannah spent on rides
    rides_cost = money / 2

    # Calculate the amount of money Hannah spent on dessert
    dessert_cost = 5

    # Calculate the amount of money Hannah has left
    money_left = money - rides_cost - dessert_cost

    # return the result
    result = money_left
    return result

print(solution())