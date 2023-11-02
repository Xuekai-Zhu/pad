def solution():
    """Marie is planning to buy a new cash register for her bakery that costs $1040. Every day Marie sells 40 loaves of bread for $2 each and 6 cakes for $12 each. She has to pay $20 each day for rent and $2 each day for electricity. How many days' worth of profits will it take for Marie to pay for the cash register?"""
    register_cost = 1040
    bread_sold = 40
    bread_price = 2
    cakes_sold = 6
    cake_price = 12
    rent_cost = 20
    electricity_cost = 2
    
    daily_profit = (bread_sold * bread_price) + (cakes_sold * cake_price) - rent_cost - electricity_cost
    days_to_pay_register = register_cost / daily_profit
    result = days_to_pay_register
    return result

print(solution())