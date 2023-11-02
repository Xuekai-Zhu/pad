def solution():
    # Calculate the total number of peppers previously bought
    previous_peppers = (30 * 3) + (30 * 2) + (10 * 1)  

    # Calculate the total number of peppers currently bought
    current_peppers = (15 * 2) + (90 * 1)  

    # Calculate the difference in peppers bought
    difference = previous_peppers - current_peppers
    result = difference
    return result

print(solution())