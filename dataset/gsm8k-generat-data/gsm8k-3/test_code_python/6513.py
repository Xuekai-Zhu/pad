def solution():
    """Julio goes fishing and can catch 7 fish every hour. By the 9th hour, how many fish does Julio have if he loses 15 fish in the process?"""
    # Define the number of fish Julio can catch per hour
    FISH_PER_HOUR = 7

    # Define the number of hours Julio fishes
    hours_fished = 9

    # Calculate the total number of fish Julio catches
    total_fish = FISH_PER_HOUR * hours_fished

    # Subtract the number of fish Julio lost
    total_fish -= 15

    # Display the total number of fish Julio has
    result = total_fish
    return result

print(solution())