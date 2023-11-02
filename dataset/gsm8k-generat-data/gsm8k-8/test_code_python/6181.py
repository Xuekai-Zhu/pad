def solution():
    # Calculate the total number of pills from the bottles with 120 pills
    total_120 = 3 * 120

    # Calculate the total number of pills from the bottles with 30 pills
    total_30 = 2 * 30

    # Calculate the total number of pills Antonia has after filling her pillbox for 2 weeks
    total_used = 5 * 14

    # Calculate the total number of pills left
    total_left = total_120 + total_30 - total_used
    result = total_left
    return result

print(solution())