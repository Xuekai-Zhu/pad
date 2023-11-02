def solution():
    # Calculate the total number of lines in the sonnets Horatio wrote
    total_lines = 70

    # Calculate the number of lines in one sonnet
    lines_per_sonnet = 14

    # Calculate the total number of sonnets
    total_sonnets = (total_lines / lines_per_sonnet) + 7

    result = total_sonnets
    return result

print(solution())