def solution():
    # Define the cost of the sneakers and the amount already saved
    sneaker_cost = 90
    saved_amount = 15

    # Calculate the amount needed from selling action figures
    needed_amount = sneaker_cost - saved_amount - 25

    # Calculate the price per action figure
    price_per_figure = needed_amount / 10
    result = price_per_figure
    return result

print(solution())