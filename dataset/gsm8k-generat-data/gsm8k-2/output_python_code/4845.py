def solution():
    """Under standard growth conditions, the bacterial strain, E.coli, has a doubling time of 20 minutes. If 1 single bacterial cell is used to start a culture grown under standard growth conditions, how many bacterial cells will there be after the culture is grown for 4 hours?"""
    initial_cells = 1
    doubling_time = 20
    growth_periods = 4 * 60 // doubling_time  # 4 hours converted to minutes, divided by doubling time
    final_cells = initial_cells * 2 ** growth_periods
    result = final_cells
    return result

print(solution())