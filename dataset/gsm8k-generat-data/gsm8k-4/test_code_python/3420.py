def solution():
    """Jimmy has a collection of 5 action figures. Each figure is worth $15, except for one which is worth $20. He decided to sell his collection. To do it fast he decided to sell each of them for $5 less than their value. How much will Jimmy earn if he sells all the figures?"""
    # Define the value of each figure
    figure_value = 15

    # Define the value of the special figure
    special_figure_value = 20

    # Define the number of figures
    num_figures = 5

    # Calculate the total value of all figures
    total_value = (num_figures - 1) * figure_value + special_figure_value

    # Calculate the amount Jimmy will earn by selling each figure for $5 less than its value
    selling_price = figure_value - 5
    total_sales = num_figures * selling_price

    # Calculate Jimmy's earnings
    earnings = total_sales - total_value

    # Display Jimmy's earnings
    result = earnings
    return result

print(solution())