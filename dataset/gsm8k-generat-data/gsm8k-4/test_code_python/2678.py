def solution():
    """Nunzio eats three pieces of pizza every day for lunch. If a piece of pizza represents one-eighth of the entire pie, then how many pizzas does Nunzio eat in 72 days?"""
    # Calculate the number of pizzas Nunzio eats per day
    pizzas_per_day = 3 / 8

    # Calculate the total number of pizzas Nunzio eats in 72 days
    total_pizzas = pizzas_per_day * 72

    # Round the result to the nearest whole number
    result = round(total_pizzas)
    return result

print(solution())