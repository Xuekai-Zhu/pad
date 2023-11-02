def solution():
    # Calculate the total number of peppers previously bought
    previous_total_peppers = (30 * 3) + (30 * 2) + (10 * 1)

    # Calculate the total number of peppers now bought
    current_total_peppers = (15 * 2) + (90 * 1)

    # Calculate the difference in the number of peppers bought
    difference = previous_total_peppers - current_total_peppers
    result = difference
    return result

print(solution())