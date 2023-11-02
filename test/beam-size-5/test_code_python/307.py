def solution():
    
    # Define the number of days in a week
    DAYS_IN_WEEK = 7

    # Define the number of eggs eaten by the three people each day
    eggs_3 = 3

    # Define the number of eggs eaten by the rest of the people each day
    eggs_rest = 2

    # Calculate the total number of eggs eaten in a week
    total_eggs = (eggs_3 * DAYS_IN_WEEK) + (eggs_rest * DAYS_IN_WEEK)

    # Display the total number of eggs eaten in a week
    result = total_eggs
    return result

print(solution())