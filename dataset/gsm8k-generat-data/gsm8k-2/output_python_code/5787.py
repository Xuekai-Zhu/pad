def solution():
    """Some friends went hiking for 3.5 hours. They traveled 21 kilometers in that time. Birgit was 4 minutes/km faster than the average time. If Birgit kept the same pace, how many minutes would it take her to go 8 kilometers?"""
    total_time = 3.5 * 60  # convert to minutes
    total_distance = 21
    average_speed = total_distance / total_time
    birgit_speed = average_speed - (4 / 60)  # convert 4 min to hours
    birgit_time = (8 / birgit_speed)
    result = birgit_time * 60  # convert back to minutes
    return result

print(solution())