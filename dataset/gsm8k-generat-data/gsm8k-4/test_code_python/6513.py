def solution():
    """Julio goes fishing and can catch 7 fish every hour. By the 9th hour, how many fish does Julio have if he loses 15 fish in the process?"""
    # Define the number of fish Julio can catch per hour and the total hours spent fishing
    FISH_PER_HOUR = 7
    TOTAL_HOURS = 9

    # Define the number of fish lost during the fishing trip
    FISH_LOST = 15

    # Calculate the total number of fish caught
    total_fish = FISH_PER_HOUR * TOTAL_HOURS

    # Subtract the lost fish from the total catch
    total_fish -= FISH_LOST

    result = total_fish
    return result

print(solution())