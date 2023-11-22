def solution():
    
    # Define the number of eggs produced by each type of chicken per day
    RED_EGGS_PER_DAY = 3
    WHITE_EGGS_PER_DAY = 5

    # Define the number of days Jerry collects eggs every day
    DAYS_PER_DAY = 42

    # Calculate the total number of eggs produced by the red chickens
    red_eggs = RED_EGGS_PER_DAY * DAYS_PER_DAY * 2

    # Calculate the total number of eggs produced by the white chickens
    white_eggs = WHITE_EGGS_PER_DAY * DAYS_PER_DAY * 2

    # Calculate the total number of eggs collected by Jerry's flock
    total_eggs = red_eggs + white_eggs

    # Calculate the number of red chickens
    red_chickens = total_eggs - total_eggs

    # Display the number of red chickens
    result = red_chickens
    return result

print(solution())