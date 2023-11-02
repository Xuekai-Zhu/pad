def solution():
    # Calculate the number of action figures sold at the pawnshop
    sold_figures = 24 * (1/4)  

    # Calculate the number of remaining action figures
    remaining_figures = 24 - sold_figures  

    # Calculate the number of action figures given to Angela's daughter
    daughter_figures = remaining_figures * (1/3)  

    # Calculate the number of action figures Angela has left
    left_figures = remaining_figures - daughter_figures  

    result = left_figures
    return result

print(solution())