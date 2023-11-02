def solution():
    """Jesse and Mia are competing in a week long race. They have one week to run 30 miles. On the first three days Jesse averages (2/3) of a mile. On day four she runs 10 miles. Mia averages 3 miles a day over the first 4 days. What is the average of their average that they have to run over the final three days?"""
    # Define the total distance to run and the distances run by Jesse and Mia in the first 4 days
    total_distance = 30
    jesse_distance = (2/3) * 3 + 10
    mia_distance = 3 * 4

    # Calculate the remaining distance for both Jesse and Mia
    jesse_remaining_distance = total_distance - jesse_distance
    mia_remaining_distance = total_distance - mia_distance

    # Calculate the average distance each of them needs to run per day for the remaining days
    jesse_average = jesse_remaining_distance / 3
    mia_average = mia_remaining_distance / 3

    # Calculate the average of their averages
    average_of_averages = (jesse_average + mia_average) / 2

    result = average_of_averages
    return result

print(solution())