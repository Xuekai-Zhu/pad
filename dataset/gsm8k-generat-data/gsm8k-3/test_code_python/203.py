def solution():
    """Benny bought 2 soft drinks for $4 each and 5 candy bars. He spent a total of 28 dollars. How much did each candy bar cost?"""
    # Define the cost of each soft drink
    drink_cost = 4

    # Define the total number of drinks purchased
    total_drinks = 2

    # Define the total number of candy bars purchased
    total_candy_bars = 5

    # Define the total cost of the drinks
    drinks_cost = drink_cost * total_drinks

    # Define the total cost of the candy bars
    total_cost = 28
    candy_bars_cost = total_cost - drinks_cost

    # Calculate the cost of each candy bar
    candy_bar_cost = candy_bars_cost / total_candy_bars

    # Return the result
    result = candy_bar_cost
    return result

print(solution())