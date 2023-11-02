def solution():
    """In a car racing competition, Skye drove a 6-kilometer track. For the first 3 kilometers, his speed was 150 kilometers per hour. For the next 2 kilometers, his speed was 50 kilometers per hour more. For the remaining 1 kilometer, his speed was twice as fast as his speed on the first 3 kilometers. What is Skye's average speed for the entire race?"""
    first_segment_distance = 3
    first_segment_speed = 150
    second_segment_distance = 2
    second_segment_speed = first_segment_speed + 50
    third_segment_distance = 1
    third_segment_speed = 2 * first_segment_speed

    total_distance = first_segment_distance + second_segment_distance + third_segment_distance
    total_time = (first_segment_distance / first_segment_speed) + (second_segment_distance / second_segment_speed) + (
            third_segment_distance / third_segment_speed)
    average_speed = total_distance / total_time
    result = average_speed
    return result

print(solution())