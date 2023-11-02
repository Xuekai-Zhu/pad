def solution():
    cost_of_sneakers = 90
    amount_saved = 15
    amount_left = 25
    num_action_figures = 10

    # Calculate the amount Lee needs to make from selling his action figures
    amount_to_make = cost_of_sneakers - amount_saved - amount_left

    # Calculate the price per action figure
    price_per_figure = amount_to_make / num_action_figures
    result = price_per_figure
    return result

print(solution())