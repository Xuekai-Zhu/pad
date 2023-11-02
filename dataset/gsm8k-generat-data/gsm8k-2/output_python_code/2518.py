def solution():
    """Lee is saving up for a new pair of sneakers which cost $90. He already has $15 saved. He plans to sell his old action figures to make the rest. If he sells 10 action figures and still has $25 left after buying the sneakers how much did he charge per action figure?"""
    total_cost = 90
    current_savings = 15
    remaining_cost = total_cost - current_savings
    action_figure_proceeds = remaining_cost - 25
    action_figure_price = action_figure_proceeds / 10
    result = round(action_figure_price, 2)
    return result

print(solution())