def solution():
    # Calculate how much distance Jesse covered in the first 3 days
    jesse_cumulative_distance = (2/3) * 3
    # Calculate how much distance Jesse needs to cover in the final 3 days
    jesse_remaining_distance = 30 - jesse_cumulative_distance - 10

    # Calculate how much distance Mia covered in the first 4 days
    mia_cumulative_distance = 3 * 4
    # Calculate how much distance Mia needs to cover in the final 3 days
    mia_remaining_distance = 30 - mia_cumulative_distance

    # Calculate the average of their remaining distances
    average_remaining_distance = (jesse_remaining_distance + mia_remaining_distance) / 2

    # Calculate the average of their averages
    average_of_averages = (jesse_cumulative_distance/3 + mia_cumulative_distance/4 + average_remaining_distance/3) / 3

    return average_of_averages

print(solution())