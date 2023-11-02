def solution():
    # Calculate the total amount of money Lee needs to buy the sneakers
    total_cost = 90  

    # Calculate the total amount of money Lee has after selling his action figures
    total_money = total_cost + 25 - 15  # Lee has $25 left after buying the sneakers and he already had $15 saved

    # Calculate the amount of money Lee got for each action figure
    price_per_action_figure = total_money / 10

    result = price_per_action_figure
    return result

print(solution())