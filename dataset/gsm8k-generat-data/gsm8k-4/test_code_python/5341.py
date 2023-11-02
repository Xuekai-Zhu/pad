def solution():
    """Mark is 5 feet 3 inches tall and Mike is 6 feet and 1 inch tall. How much taller is Mike than Mark in inches if 1 foot is equal to 12 inches?"""
    # Define Mark's height in inches
    mark_height = 5 * 12 + 3

    # Define Mike's height in inches
    mike_height = 6 * 12 + 1

    # Calculate the height difference in inches
    height_difference = mike_height - mark_height

    result = height_difference
    return result

print(solution())