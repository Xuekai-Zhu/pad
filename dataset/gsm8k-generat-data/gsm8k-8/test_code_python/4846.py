def solution():
    # Calculate how many doubling periods occur in 4 hours (240 minutes)
    doubling_periods = 240 / 20

    # Calculate the final number of bacterial cells using the formula N = 2^n, where n is the number of doubling periods
    final_cells = 2 ** doubling_periods

    result = final_cells
    return result

print(solution())