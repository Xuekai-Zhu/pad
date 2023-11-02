def solution():
    """Lee is saving up for a new pair of sneakers which cost $90. He already has $15 saved. He plans to sell his old action figures to make the rest. If he sells 10 action figures and still has $25 left after buying the sneakers how much did he charge per action figure?"""
    # Define the total cost of the sneakers
    total_cost = 90

    # Define the amount Lee has saved and the amount he needs to earn from selling his action figures
    saved_amount = 15
    action_figures_amount = total_cost - saved_amount - 25

    # Calculate the price per action figure
    price_per_figures = action_figures_amount / 10

    # Return the result
    result = price_per_figures
    return result

print(solution())