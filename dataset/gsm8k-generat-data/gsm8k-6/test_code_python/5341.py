def solution():
    # Convert Mark's height to inches
    mark_height_inches = (5*12) + 3  # 5 feet and 3 inches

    # Convert Mike's height to inches
    mike_height_inches = (6*12) + 1  # 6 feet and 1 inch

    # Calculate the height difference in inches
    height_difference_inches = mike_height_inches - mark_height_inches

    result = height_difference_inches
    return result

print(solution())