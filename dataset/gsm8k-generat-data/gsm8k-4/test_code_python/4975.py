def solution():
    """Angela has a collection of 24 pieces of rare action figures. She sold off a quarter of them at the pawnshop and gave one-third of the remainder to her daughter. How many does she have left?"""
    # Define the initial number of action figures
    initial_figures = 24

    # Calculate the number of action figures sold at the pawnshop
    sold_figures = initial_figures / 4

    # Calculate the number of action figures remaining
    remaining_figures = initial_figures - sold_figures

    # Calculate the number of action figures given to her daughter
    daughter_figures = remaining_figures / 3

    # Calculate the final number of action figures
    final_figures = remaining_figures - daughter_figures

    result = final_figures
    return result

print(solution())