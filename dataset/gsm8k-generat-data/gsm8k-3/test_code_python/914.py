def solution():
    """There are six more white birds next to a cage than grey birds in the cage. If the number of grey birds in the cage is 40, and after ten minutes, half of the birds in the cage are freed and fly away, calculate the total number of birds remaining."""
    # Calculate the number of white birds next to the cage
    white_birds = 40 + 6

    # Calculate the total number of birds in the cage
    total_birds = 40 + white_birds

    # Calculate the number of birds that fly away
    flying_birds = total_birds // 2

    # Calculate the number of birds remaining
    remaining_birds = total_birds - flying_birds

    # Display the number of birds remaining
    result = remaining_birds
    return result

print(solution())