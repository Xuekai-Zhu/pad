def solution():
    # Calculate the number of doublings in 4 hours (240 minutes)
    doublings = int(240 / 20)

    # Calculate the final number of bacterial cells
    final_cells = 2 ** doublings

    result = final_cells
    return result

print(solution())