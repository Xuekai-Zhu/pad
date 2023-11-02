def solution():
    
    cost_of_sneakers = 90
    amount_saved = 15
    amount_needed = cost_of_sneakers - amount_saved
    amount_left = 25
    num_action_figures = 10
    price_per_figure = (amount_needed + amount_left) / num_action_figures
    result = price_per_figure
    return result

print(solution())