def solution():
    calories_per_orange = 80  # Oranges have 80 calories each
    cost_per_orange = 1.2  # Oranges cost $1.20 each
    budget = 10  # Timmy has $10 to spend
    required_calories = 400  # Timmy needs to consume 400 calories

    # Calculate the number of oranges Timmy needs to buy to get 400 calories
    oranges_required = required_calories / calories_per_orange

    # Calculate the cost of the oranges Timmy needs to buy
    cost_required = oranges_required * cost_per_orange

    # Calculate the amount of money Timmy will have left after he buys the oranges
    money_left = budget - cost_required
    result = money_left
    return result

print(solution())