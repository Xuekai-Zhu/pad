def solution():
    """For football season, Zachary wants to buy a new football, a pair of shorts, and a pair of football shoes. The ball costs $3.75, the shorts cost $2.40, and the shoes cost $11.85. Zachary has $10. How much more money does Zachary need?"""
    # Define the prices of the football, shorts, and shoes
    football_price = 3.75
    shorts_price = 2.40
    shoes_price = 11.85

    # Define the total amount of money Zachary has
    zachary_money = 10

    # Calculate the total cost of the items
    total_cost = football_price + shorts_price + shoes_price

    # Calculate how much more money Zachary needs
    more_money = total_cost - zachary_money

    # return the result
    result = more_money
    return result

print(solution())