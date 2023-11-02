def solution():
    # Calculate the total dozens of eggs sold in four weeks
    total_dozens = 120 / 3  

    # Calculate the total number of eggs sold in four weeks
    total_eggs = total_dozens * 12

    # Calculate the average number of eggs each hen lays per week
    eggs_per_week_per_hen = total_eggs / (10 * 4)

    result = eggs_per_week_per_hen
    return result

print(solution())