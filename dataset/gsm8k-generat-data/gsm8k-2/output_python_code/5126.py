def solution():
    """The Early Bird Dinner offered dinner meals at half off the menu price if you eat between 2-4 pm. Curtis ordered the Salisbury Steak that costs $16.00 and Rob ordered the Chicken Fried Steak at $18.00. If they ate at 3 pm, what was the cost of their total bill?"""
    curtis_meal_price = 16
    rob_meal_price = 18
    discount = 0.5
    total_cost = (curtis_meal_price + rob_meal_price) * discount
    result = total_cost
    return result

print(solution())