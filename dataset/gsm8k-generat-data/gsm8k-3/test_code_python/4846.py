def solution():
    """Under standard growth conditions, the bacterial strain, E.coli, has a doubling time of 20 minutes.   If 1 single bacterial cell is used to start a culture grown under standard growth conditions, how many bacterial cells will there be after the culture is grown for 4 hours?"""
    
    # Each doubling time is 20 minutes
    # There are 4 * 60 = 240 minutes in 4 hours
    # Therefore, there are 240 / 20 = 12 doubling periods
    
    # Calculate the final number of cells
    final_cells = 2 ** 12
    
    # Since we started with one cell, the total number of cells is the final number of cells plus the initial cell
    total_cells = final_cells + 1
    
    result = total_cells
    return result

print(solution())