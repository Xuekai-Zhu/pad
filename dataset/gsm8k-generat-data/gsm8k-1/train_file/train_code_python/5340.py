def solution():
    """Mark is 5 feet 3 inches tall and Mike is 6 feet and 1 inch tall. How much taller is Mike than Mark in inches if 1 foot is equal to 12 inches?"""
    mark_height_inches = 5 * 12 + 3
    mike_height_inches = 6 * 12 + 1
    difference_inches = mike_height_inches - mark_height_inches
    result = difference_inches
    return result

print(solution())