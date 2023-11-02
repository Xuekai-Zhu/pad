def solution():
    # Calculate the total vertical distance Jack traveled in inches
    total_distance = (3 * 12 * 8) - (6 * 12 * 8)

    # Convert the distance to feet and take the absolute value
    distance_in_feet = abs(total_distance / 12)

    result = distance_in_feet
    return result

print(solution())