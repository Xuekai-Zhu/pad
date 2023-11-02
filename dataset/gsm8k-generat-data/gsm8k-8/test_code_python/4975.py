def solution():
    # Define the initial number of action figures
    num_figures = 24

    # Calculate the number sold at the pawnshop
    sold_figures = num_figures / 4

    # Calculate the remaining number of figures
    remaining_figures = num_figures - sold_figures

    # Calculate the number given to her daughter
    daughter_figures = remaining_figures / 3

    # Calculate the final number of figures Angela has left
    final_figures = remaining_figures - daughter_figures
    result = final_figures
    return result

print(solution())