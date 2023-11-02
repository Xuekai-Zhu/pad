def solution():
    # Define the initial number of action figures
    initial_figures = 10

    # Calculate the new number of action figures after selling and buying
    new_figures = initial_figures - 6 + 4

    # Calculate the size of the brother's collection
    brother_collection = 2 * new_figures

    # Calculate the total number of action figures
    total_figures = new_figures + brother_collection
    result = total_figures
    return result

print(solution())