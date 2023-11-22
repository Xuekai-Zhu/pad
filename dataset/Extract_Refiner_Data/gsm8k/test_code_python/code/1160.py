def solution():
    
    # Define the number of eggs in a dozen
    EGGS_PER_DOZEN = 12

    # Define the initial number of eggs
    initial_eggs = 3 * EGGS_PER_DOZEN

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

    # Calculate the number of eggs that are still hidden
    hidden_eggs = initial_eggs - total_eggs

    # Display the number

print(solution())