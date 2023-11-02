def solution():
    
    # Define the number of eggs produced by each type of chicken per day
    RED_EGGS_PER_DAY = 3
    WHITE_EGGS_PER_DAY = 5

    # Define the number of days Jerry collects eggs
    DAYS = 42

    # Calculate the total number of red chickens
    red_chickens = RED_EGGS_PER_DAY * DAYS

    # Calculate the total number of white chickens
    white_chickens = WHITE_EGGS_PER_DAY * DAYS

    # Calculate the total number of eggs collected
    total_eggs = red_chickens + white_chickens

    # Calculate the number of white chickens
    white_chickens = (total_eggs - 2) / WHITE_EGGS_PER_DAY

    # Calculate the total number of red chickens
    red_chickens = red_chickens + white_chickens

    # Display the total number of red chickens
    result = red_chick

print(solution())