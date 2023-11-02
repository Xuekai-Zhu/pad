def solution():
    
    # Define the number of eggs in a dozen
    EGGS_PER_DOZEN = 12

    # Define the number of eggs found by Lamar
    lamar_eggs = 5

    # Define the number of eggs found by Stacy
    stacy_eggs = lamar_eggs * 2

    # Define the number of eggs found by Charlie
    charlie_eggs = stacy_eggs - 2

    # Define the number of eggs found by Mei
    mei_eggs = charlie_eggs / 2

    # Calculate the total number of eggs found
    total_eggs = lamar_eggs + stacy_eggs + charlie_eggs + mei_eggs

    # Calculate the number of eggs still hidden
    eggs_hidden = EGGS_PER_DOZEN - total_eggs

    # Display the number of eggs still hidden
    result = eggs_hidden
    return result

print(solution())