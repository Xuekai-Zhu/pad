def solution():
    
    # Define the number of eggs per omelet and the number of days in a week
    EGGS_PER_OMELET = 3
    DAYS_PER_WEEK = 7

    # Calculate the total number of eggs in 4 weeks
    total_eggs = EGGS_PER_OMELET * DAYS_PER_WEEK * 4

    # Calculate the number of dozens of eggs
    dozens = total_eggs / 12

    # Display the number of dozens
    result = dozens
    return result

print(solution())