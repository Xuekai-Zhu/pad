def solution():
    # Number of eggs found by each child
    kevin_eggs = 5
    bonnie_eggs = 13
    george_eggs = 9
    cheryl_eggs = 56

    # Total number of eggs found by the other three children
    other_eggs = kevin_eggs + bonnie_eggs + george_eggs

    # Difference between Cheryl's eggs and the other three children's eggs
    difference = cheryl_eggs - other_eggs
    result = difference
    return result

print(solution())