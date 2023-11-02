def solution():
    """Hannah wanted to make an apple pie that would serve 8 people. She needed 2 pounds of apples that were on sale for $2.00 per pound. The pre-made pie crust cost $2.00. The lemon cost $.50 and the butter cost $1.50. How much did each serving of pie cost?"""
    # Define the cost of the apples and the ingredients for the pie
    apple_cost = 2.00 * 2
    crust_cost = 2.00
    lemon_cost = 0.50
    butter_cost = 1.50

    # Calculate the total cost of the pie
    total_cost = apple_cost + crust_cost + lemon_cost + butter_cost

    # Calculate the cost per serving
    cost_per_serving = total_cost / 8

    # Return the result rounded to 2 decimal places
    result = round(cost_per_serving, 2)
    return result

print(solution())