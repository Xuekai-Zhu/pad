def solution():
    num_people = 8  # The apple pie is meant to serve 8 people
    apple_price_per_lb = 2.00  # The apples are on sale for $2.00 per pound
    apple_weight = 2  # Hannah needs 2 pounds of apples for the pie
    crust_price = 2.00  # The pre-made pie crust costs $2.00
    lemon_price = 0.50  # The lemon costs $0.50
    butter_price = 1.50  # The butter costs $1.50

    # Calculate the total cost of making the apple pie
    total_cost = (apple_price_per_lb * apple_weight) + crust_price + lemon_price + butter_price

    # Calculate the cost per serving of the apple pie
    cost_per_serving = total_cost / num_people
    result = cost_per_serving
    return result

print(solution())