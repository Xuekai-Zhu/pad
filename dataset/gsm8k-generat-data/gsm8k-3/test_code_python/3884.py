def solution():
    """During the Easter egg hunt, Kevin found 5 eggs, Bonnie found 13 eggs, George found 9 and Cheryl found 56.  How many more eggs did Cheryl find than the other three children found?"""
    # Define the number of eggs found by each child
    kevin_eggs = 5
    bonnie_eggs = 13
    george_eggs = 9
    cheryl_eggs = 56

    # Calculate the total number of eggs found by the other three children
    other_eggs = kevin_eggs + bonnie_eggs + george_eggs

    # Calculate the number of eggs Cheryl found more than the other three children
    difference = cheryl_eggs - other_eggs

    # Display the difference in the number of eggs found
    result = difference
    return result

print(solution())