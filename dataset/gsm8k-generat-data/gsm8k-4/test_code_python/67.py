def solution():
    """Jesse and Mia are competing in a week long race. They have one week to run 30 miles. On the first three days Jesse averages (2/3) of a mile. On day four she runs 10 miles. Mia averages 3 miles a day over the first 4 days. What is the average of their average that they have to run over the final three days?"""
    # Calculate the total distance covered by Jesse on the first four days
    jesse_distance_covered = (2/3) * 3 + 10

    # Calculate the total distance covered by Mia on the first four days
    mia_distance_covered = 3 * 4

    # Calculate the total distance left to cover
    total_distance_left = 30 - jesse_distance_covered - mia_distance_covered

    # Calculate the average distance that needs to be covered by both Jesse and Mia over the final three days
    average_distance_left = total_distance_left / 6

    # Calculate the average of their averages
    average_of_averages = (2/3 + 3 + average_distance_left) / 3

    result = average_of_averages
    return result

print(solution())