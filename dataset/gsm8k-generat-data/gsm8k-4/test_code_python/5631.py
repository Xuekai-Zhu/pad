def solution():
    """Kim takes 4 classes in school that last 2 hours each. She drops 1 class. How many hours of classes does she have now have per day?"""
    # Calculate the total hours for all 4 classes
    total_hours = 4 * 2

    # Subtract the hours for the dropped class
    remaining_hours = total_hours - 2

    # Calculate the hours per day
    hours_per_day = remaining_hours / 3

    result = hours_per_day
    return result

print(solution())