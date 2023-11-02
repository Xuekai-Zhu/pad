def solution():
    """Lee is saving up for a new pair of sneakers which cost $90. He already has $15 saved. He plans to sell his old
    action figures to make the rest. If he sells 10 action figures and still has $25 left after buying the sneakers how
    much did he charge per action figure?"""
    # Define the cost of the sneakers and the amount Lee has saved
    sneaker_cost = 90
    saved_amount = 15

    # Calculate the amount Lee needs to earn from selling his action figures
    needed_amount = sneaker_cost - saved_amount - 25

    # Calculate the cost per action figure using the number of action figures sold
    action_figures = 10
    cost_per_figure = needed_amount / action_figures

    # Display the cost per action figure
    result = cost_per_figure
    return result

print(solution())