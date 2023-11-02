def solution():
    total_time = 3 * 60  # 3 hours converted to minutes
    num_talking_segments = 3
    talking_segment_length = 10
    num_ad_breaks = 5
    ad_break_length = 5

    # Calculate the total time taken by talking segments
    talking_time = num_talking_segments * talking_segment_length

    # Calculate the total time taken by ad breaks
    ad_break_time = num_ad_breaks * ad_break_length

    # Calculate the remaining time for playing songs
    remaining_time = total_time - talking_time - ad_break_time
    result = remaining_time
    return result

print(solution())