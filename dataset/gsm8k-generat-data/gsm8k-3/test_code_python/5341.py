def solution():
    """Mark is 5 feet 3 inches tall and Mike is 6 feet and 1 inch tall. How much taller is Mike than Mark in inches if 1 foot is equal to 12 inches?"""
    # Convert Mark's height to inches
    mark_height = 5 * 12 + 3

    # Convert Mike's height to inches
    mike_height = 6 * 12 + 1

    # Calculate the height difference in inches
    height_diff = mike_height - mark_height

    # Display the height difference in inches
    result = height_diff
    return result

print(solution())