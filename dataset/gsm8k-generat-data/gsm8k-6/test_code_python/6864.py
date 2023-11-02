def solution():
    # Calculate the total number of paper cups prepared
    total_cups = 4 * 2 * 12  # four sets of 2-dozen paper cups

    # Calculate the number of cups used
    cups_used = total_cups - 5 - 30  # five cups were damaged, 30 were not used

    result = cups_used
    return result

print(solution())