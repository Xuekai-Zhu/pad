def solution():
    # Define the number of toys and the fraction that are action figures
    total_toys = 24
    action_figure_fraction = 1/4

    # Calculate the number of action figures and dolls
    num_action_figures = total_toys * action_figure_fraction
    num_dolls = total_toys - num_action_figures

    result = num_dolls
    return result

print(solution())