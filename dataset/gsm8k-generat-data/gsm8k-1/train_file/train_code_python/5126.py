def solution():
    """The Early Bird Dinner offered dinner meals at half off the menu price if you eat between 2-4 pm. Curtis ordered the Salisbury Steak that costs $16.00 and Rob ordered the Chicken Fried Steak at $18.00. If they ate at 3 pm, what was the cost of their total bill?"""
    curtis_meal_price = 16.00
    rob_meal_price = 18.00
    discount_percent = 50
    total_meal_price = curtis_meal_price + rob_meal_price
    discounted_meal_price = total_meal_price * (discount_percent / 100)
    final_bill = discounted_meal_price
    return final_bill

print(solution())