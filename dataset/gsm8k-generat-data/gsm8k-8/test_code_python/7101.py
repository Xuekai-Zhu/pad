def solution():
    # Calculate Monday's pints
    monday_pints = 4 * 3

    # Calculate Tuesday's pints
    tuesday_pints = monday_pints / 3

    # Calculate Wednesday's pints
    wednesday_pints = monday_pints / 2

    # Calculate the total pints
    total_pints = 4 + monday_pints + tuesday_pints + wednesday_pints
    result = total_pints
    return result

print(solution())