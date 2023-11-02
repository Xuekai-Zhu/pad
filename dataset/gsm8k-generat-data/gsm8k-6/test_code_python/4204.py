def solution():
    # Calculate the number of feet Alexander grows in 4 years
    feet_grown = 4 * 1/2

    # Convert feet to inches and add to his initial height of 50 inches
    total_height = (feet_grown * 12) + 50

    result = total_height
    return result

print(solution())