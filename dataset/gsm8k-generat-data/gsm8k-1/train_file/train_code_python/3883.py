def solution():
    """During the Easter egg hunt, Kevin found 5 eggs, Bonnie found 13 eggs, George found 9 and Cheryl found 56. How many more eggs did Cheryl find than the other three children found?"""
    kevin_eggs = 5
    bonnie_eggs = 13
    george_eggs = 9
    cheryl_eggs = 56
    total_eggs = kevin_eggs + bonnie_eggs + george_eggs
    difference = cheryl_eggs - total_eggs
    result = difference
    return result

print(solution())