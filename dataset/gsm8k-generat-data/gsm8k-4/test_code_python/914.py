def solution():
    """There are six more white birds next to a cage than grey birds in the cage. If the number of grey birds in the cage is 40, and after ten minutes, half of the birds in the cage are freed and fly away, calculate the total number of birds remaining."""
    # Define the number of grey birds
    grey_birds = 40

    # Calculate the number of white birds
    white_birds = grey_birds + 6

    # Calculate the initial total number of birds
    total_birds = grey_birds + white_birds

    # Calculate the number of birds that flew away
    flown_birds = total_birds // 2

    # Calculate the number of remaining birds
    remaining_birds = total_birds - flown_birds

    result = remaining_birds
    return result

print(solution())