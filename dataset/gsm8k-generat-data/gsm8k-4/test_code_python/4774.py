def solution():
    """Two athletes decided to compete to see who had the best jumping ability. They were each going to do the long jump, triple jump, and high jump to see who had the highest average jump. The first athlete jumped 26 feet in the long jump, 30 feet in the triple jump, and 7 feet in the high jump. The second athlete jumped 24 feet in the long jump, 34 feet in the triple jump, and 8 feet in the high jump. What was the average jump of the winner?"""
    # Calculate the total distance jumped by the first athlete
    first_total_distance = 26 + 30 + 7

    # Calculate the total distance jumped by the second athlete
    second_total_distance = 24 + 34 + 8

    # Calculate the average jump of each athlete
    first_average = first_total_distance / 3
    second_average = second_total_distance / 3

    # Determine which athlete had the highest average jump
    if first_average > second_average:
        winner_average = first_average
    else:
        winner_average = second_average

    result = winner_average
    return result

print(solution())