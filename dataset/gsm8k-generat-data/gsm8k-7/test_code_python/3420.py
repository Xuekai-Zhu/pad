def solution():
    num_figures = 5
    value_per_figure = 15
    higher_value_figure = 20
    discount = 5

    # Calculate the total value of all figures
    total_value = (num_figures - 1) * value_per_figure + higher_value_figure

    # Calculate the total earned by selling all figures
    total_earned = num_figures * (value_per_figure - discount)

    result = total_earned
    return result

print(solution())