def solution():
    
    # Define the number of toothpicks needed and the number of weeks it takes to save enough to get 200 toothpicks
    TOTAL_TOOTHPASTES = 200
    WEEKS_SAVED = 10

    # Initialize the number of weeks and the number of toothpicks saved each week
    weeks = 12
    toothpicks_saved = 0

    # Keep saving until there are enough to save enough to get 200 toothpicks
    while toothpicks_saved < TOTAL_TOOTHPASTES:
        # Increment the number of weeks and save the remaining toothpicks
        weeks += 1
        toothpicks_saved += 10

    # Display the number of weeks it took to save enough to get 200 toothpicks
    result = weeks
    return result

print(solution())