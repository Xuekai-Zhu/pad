def solution():
    lines_per_sonnet = 14
    lines_unheard = 70

    # Calculate the total number of lines of poetry Horatio wrote
    total_lines = lines_unheard + (7 * lines_per_sonnet)

    # Calculate the total number of sonnets Horatio wrote by dividing total_lines by lines_per_sonnet
    total_sonnets = total_lines / lines_per_sonnet
    result = total_sonnets
    return result

print(solution())