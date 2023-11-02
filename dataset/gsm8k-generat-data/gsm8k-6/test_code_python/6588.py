def solution():
    # Calculate the total number of pens in the jar before any removal
    total_pens = 9 + 21 + 6

    # Calculate the number of pens left in the jar after removal
    remaining_pens = total_pens - 4 - 7  # remove 4 blue pens and 7 black pens
    result = remaining_pens
    return result

print(solution())