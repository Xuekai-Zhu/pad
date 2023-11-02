def solution():
    # Calculate how far Alex and Max are from the finish line after each change in position
    distance_to_finish_after_1st_change = 5000 - 500
    distance_to_finish_after_2nd_change = 5000 - 170
    distance_to_finish_after_3rd_change = 5000 - 440

    # Calculate how far Max is from Alex at each point in the race
    max_distance_from_alex_to_finish_after_1st_change = distance_to_finish_after_1st_change - 300
    max_distance_from_alex_to_finish_after_2nd_change = distance_to_finish_after_2nd_change + 300
    max_distance_from_alex_to_finish_after_3rd_change = distance_to_finish_after_3rd_change - 440

    # Determine how much distance Max needs to gain to catch up to Alex at each point in the race
    distance_for_max_to_catch_up_after_1st_change = max_distance_from_alex_to_finish_after_1st_change - 200
    distance_for_max_to_catch_up_after_2nd_change = max_distance_from_alex_to_finish_after_2nd_change - 200
    distance_for_max_to_catch_up_after_3rd_change = max_distance_from_alex_to_finish_after_3rd_change - 200

    # Determine the total distance Max needs to gain to catch up to Alex
    total_distance_for_max_to_catch_up = (
        distance_for_max_to_catch_up_after_1st_change
        + distance_for_max_to_catch_up_after_2nd_change
        + distance_for_max_to_catch_up_after_3rd_change
    )

    result = total_distance_for_max_to_catch_up
    return result

print(solution())