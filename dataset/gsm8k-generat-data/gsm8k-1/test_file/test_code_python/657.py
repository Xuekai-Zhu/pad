def solution():
    """Roger goes to the store to buy some coffee. The normal brand of coffee he buys cost $5 per pound. He had to buy a more expensive brand that cost 20% more since his favorite brand was sold out. He decides to buy a week's worth of coffee and he uses 1 pound of coffee per day. He also decided to buy himself a donut for $2. How much did everything cost?"""
    normal_price = 5
    increased_percent = 20
    increased_price = normal_price * (1 + (increased_percent / 100))
    pounds_per_week = 7
    total_coffee_cost = increased_price * pounds_per_week
    total_cost = total_coffee_cost + 2
    result = total_cost
    return result

print(solution())