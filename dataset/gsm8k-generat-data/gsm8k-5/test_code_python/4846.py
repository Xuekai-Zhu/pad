def solution():
    doubling_time = 20  # E. coli has a doubling time of 20 minutes
    growth_factor = 2**(240/doubling_time)  # Calculate the growth factor for 4 hours or 240 minutes

    # Calculate the number of cells in the culture after 4 hours
    initial_cells = 1  # The culture starts with 1 bacterial cell
    final_cells = initial_cells * growth_factor
    result = final_cells
    return result

print(solution())