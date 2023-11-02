def solution():
    # Calculate the total number of lines Horatio wrote
    total_lines = 70 + 14 * 7  # 70 lines were not heard plus 14 lines for each of the 7 sonnets read to the lady
    total_sonnets = total_lines // 14  # Each sonnet is 14 lines long

    result = total_sonnets
    return result

print(solution())