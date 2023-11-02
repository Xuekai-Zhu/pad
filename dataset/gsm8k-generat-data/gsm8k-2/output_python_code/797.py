def solution():
    """Patsy is gearing up for this weekend’s graduation. She needs to have 6 appetizers per each of her 30 guests. She’s making 3 dozen deviled eggs, 2 dozen pigs in a blanket and 2 dozen kebabs. How many more dozen appetizers does she need to make?"""
    total_appetizers_needed = 6 * 30
    appetizers_made = (3 + 2 + 2) * 12  # converting dozens to individual appetizers
    appetizers_left_to_make = (total_appetizers_needed - appetizers_made) / 12  # converting back to dozens
    result = appetizers_left_to_make
    return result

print(solution())