def solution():
    """Under standard growth conditions, the bacterial strain, E.coli, has a doubling time of 20 minutes. If 1 single bacterial cell is used to start a culture grown under standard growth conditions, how many bacterial cells will there be after the culture is grown for 4 hours?"""
    doubling_time = 20
    growth_period = 4 * 60  # convert hours to minutes
    num_doublings = growth_period / doubling_time
    final_num_cells = 2 ** num_doublings
    result = final_num_cells
    return result

print(solution())