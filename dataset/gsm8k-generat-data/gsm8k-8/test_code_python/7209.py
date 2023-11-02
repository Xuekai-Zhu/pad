def solution():
    # Define the cost of 1 caramel
    caramel_cost = 3

    # Calculate the cost of 1 candy bar
    candy_bar_cost = 2 * caramel_cost

    # Calculate the cost of 4 candy bars
    four_candy_bars_cost = 4 * candy_bar_cost

    # Calculate the cost of 1 cotton candy
    cotton_candy_cost = 1/2 * four_candy_bars_cost

    # Calculate the total cost of 6 candy bars, 3 caramel, and 1 cotton candy
    total_cost = 6 * candy_bar_cost + 3 * caramel_cost + 1 * cotton_candy_cost

    result = total_cost
    return result

print(solution())