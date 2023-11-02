def solution():
    friend1_time_per_mile = 21 / 3  # Friend 1's pace in minutes per mile
    friend2_time_per_mile = 24 / 3  # Friend 2's pace in minutes per mile
    total_distance = 5  # They need to run 5 miles each
    combined_time = (friend1_time_per_mile + friend2_time_per_mile) * total_distance

    result = combined_time
    return result

print(solution())