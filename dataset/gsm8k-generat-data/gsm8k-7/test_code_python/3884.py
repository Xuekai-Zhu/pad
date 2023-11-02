def solution():
    kevin_eggs = 5
    bonnie_eggs = 13
    george_eggs = 9
    cheryl_eggs = 56

    # Calculate the total number of eggs found by the three children
    total_eggs = kevin_eggs + bonnie_eggs + george_eggs

    # Calculate the number of eggs Cheryl found more than the other three children
    difference = cheryl_eggs - total_eggs
    result = difference
    return result

print(solution())