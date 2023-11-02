def solution():
    """The Early Bird Dinner offered dinner meals at half off the menu price if you eat between 2-4 pm. Curtis ordered the Salisbury Steak that costs $16.00 and Rob ordered the Chicken Fried Steak at $18.00. If they ate at 3 pm, what was the cost of their total bill?"""
    # Define the prices of the meals
    curtis_meal_price = 16
    rob_meal_price = 18

    # Calculate the discounted prices during the Early Bird Dinner
    curtis_discounted_price = curtis_meal_price / 2
    rob_discounted_price = rob_meal_price / 2

    # Calculate the total cost of the bill
    total_bill = curtis_discounted_price + rob_discounted_price

    # return the result
    result = total_bill
    return result

print(solution())