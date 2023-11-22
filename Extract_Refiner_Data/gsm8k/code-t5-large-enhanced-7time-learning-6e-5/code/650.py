def solution():
    
    # Define the number of deviled egg halves needed per guest
    EGG_HALLS_PER_GUEST = 2

    # Define the number of guests to be invited
    num_guests = 16

    # Calculate the total number of deviled egg halves needed
    total_egg_halves = num_guests * 3

    # Calculate the total number of dozens of eggs needed
    total_dozens = total_egg_halves / EGG_HALLS_PER_GUEST

    # Display the total number of dozens of eggs needed
    result = total_dozens
    return result

print(solution())