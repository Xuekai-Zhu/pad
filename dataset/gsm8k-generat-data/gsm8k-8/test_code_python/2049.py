def solution():
    # Calculate Chris's walking time to school
    chris_time = 9 / 3

    # Calculate Mark's walking time to the point where he turns around
    mark_time_to_turnaround = 3 / 3

    # Calculate Mark's walking time back home and then back to the school
    mark_time_back_and_forth = (3 + 3) / 3

    # Calculate Mark's total walking time
    mark_total_time = mark_time_to_turnaround + mark_time_back_and_forth

    # Calculate the difference in walking time between Mark and Chris
    time_difference = mark_total_time - chris_time
    result = time_difference
    return result

print(solution())