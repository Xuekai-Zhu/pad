def solution():
    """Lee is saving up for a new pair of sneakers which cost $90. He already has $15 saved. He plans to sell his old action figures to make the rest. If he sells 10 action figures and still has $25 left after buying the sneakers how much did he charge per action figure?"""
    cost_of_sneakers = 90
    amount_saved = 15
    amount_needed = cost_of_sneakers - amount_saved
    amount_left = 25
    num_action_figures = 10
    price_per_figure = (amount_needed + amount_left) / num_action_figures
    result = price_per_figure
    return result

print(solution())