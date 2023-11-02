def solution():
    """Benny bought  2 soft drinks for$ 4 each and 5 candy bars. He spent a total of 28 dollars. How much did each candy bar cost?"""
    # Define the prices of the soft drinks and the number of candy bars
    drink_price = 4
    num_candy_bars = 5

    # Calculate the total cost of the soft drinks
    total_drink_cost = 2 * drink_price

    # Calculate the remaining amount spent on candy bars
    candy_bar_cost = 28 - total_drink_cost

    # Calculate the cost per candy bar
    candy_bar_price = candy_bar_cost / num_candy_bars

    result = candy_bar_price
    return result

print(solution())