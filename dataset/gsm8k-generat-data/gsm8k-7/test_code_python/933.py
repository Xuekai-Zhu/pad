def solution():
    steps_first_staircase = 20
    steps_second_staircase = 2 * steps_first_staircase
    steps_third_staircase = steps_second_staircase - 10
    distance_per_step = 0.5

    # Calculate the total distance John climbed for each staircase
    distance_first_staircase = steps_first_staircase * distance_per_step
    distance_second_staircase = steps_second_staircase * distance_per_step
    distance_third_staircase = steps_third_staircase * distance_per_step

    # Calculate the total distance John climbed for all staircases
    total_distance = distance_first_staircase + distance_second_staircase + distance_third_staircase
    result = total_distance
    return result

print(solution())