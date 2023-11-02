def solution():
    """Under standard growth conditions, the bacterial strain, E.coli, has a doubling time of 20 minutes.   If 1 single bacterial cell is used to start a culture grown under standard growth conditions, how many bacterial cells will there be after the culture is grown for 4 hours?"""
    # Define the doubling time and the initial number of bacterial cells
    DOUBLING_TIME = 20
    INITIAL_CELLS = 1

    # Calculate the number of doublings in 4 hours
    hours_in_minutes = 4 * 60
    doublings = hours_in_minutes / DOUBLING_TIME

    # Calculate the final number of bacterial cells
    final_cells = INITIAL_CELLS * 2 ** doublings

    # Return the result
    result = final_cells
    return result

print(solution())