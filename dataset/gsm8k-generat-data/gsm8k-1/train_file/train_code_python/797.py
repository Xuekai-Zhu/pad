def solution():
    """Patsy is gearing up for this weekend’s graduation. She needs to have 6 appetizers per each of her 30 guests. She’s making 3 dozen deviled eggs, 2 dozen pigs in a blanket and 2 dozen kebabs. How many more dozen appetizers does she need to make?"""
    guests = 30
    appetizers_per_guest = 6
    total_appetizers_needed = guests * appetizers_per_guest
    appetizers_made = 3 + 2 + 2
    appetizers_needed = total_appetizers_needed - (appetizers_made * 12)
    result = appetizers_needed
    return result

print(solution())