def solution():
    mark_height = (5 * 12) + 3  # Mark is 5 feet and 3 inches tall, so his height in inches is 63 inches
    mike_height = (6 * 12) + 1  # Mike is 6 feet and 1 inch tall, so his height in inches is 73 inches

    # Calculate the difference in height between Mike and Mark in inches
    height_difference = mike_height - mark_height
    result = height_difference
    return result

print(solution())