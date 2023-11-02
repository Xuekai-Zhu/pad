def solution():
    """There are six more white birds next to a cage than grey birds in the cage. If the number of grey birds in the cage is 40, and after ten minutes, half of the birds in the cage are freed and fly away, calculate the total number of birds remaining."""
    grey_birds = 40
    white_birds = grey_birds + 6
    total_birds = grey_birds + white_birds
    remaining_birds = total_birds // 2
    result = remaining_birds
    return result

print(solution())