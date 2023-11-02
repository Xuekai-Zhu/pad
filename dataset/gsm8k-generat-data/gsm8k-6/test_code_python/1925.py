def solution():
    # Calculate the total time Tyson spent racing
    time_in_lakes = (3/3) / 3  # half of the races were in lakes; 3 miles per race divided by 3 mph = time spent per race
    time_in_ocean = (3/2.5) / 3  # half of the races were in the ocean; 3 miles per race divided by 2.5 mph = time spent per race
    total_time = 10 * (time_in_lakes + time_in_ocean)  # there were 10 total races
    result = total_time
    return result

print(solution())