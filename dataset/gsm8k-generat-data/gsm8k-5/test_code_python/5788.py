def solution():
    total_time = 3.5  # The friends went hiking for 3.5 hours
    total_distance = 21  # They traveled 21 kilometers in that time
    average_speed = total_distance / total_time  # Calculate the average speed
    birgit_speed = average_speed - (4 / 60)  # Birgit was 4 minutes/km faster than the average time

    # Calculate the time Birgit would need to go 8 kilometers at the same pace
    time_to_8k = (8 / birgit_speed) / 60  # Converted to minutes
    result = time_to_8k
    return result

print(solution())