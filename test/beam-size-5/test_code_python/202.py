def solution():
    # Calculate the total distance Micheal made in the first 4 weeks
    distance_first_four_weeks = 25 * 4

    # Calculate the total distance Micheal made in the second 2 weeks
    distance_second_four_weeks = 60 * 2

    # Calculate the total distance Micheal made in the third 3 weeks
    distance_third_four_weeks = 60 * 3

    # Calculate the total distance Micheal made in the entire bike
    total_distance = distance_first_four_weeks + distance_second_four_weeks + distance_third_four_weeks
    result = total_distance
    return result

print(solution())