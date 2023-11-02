def solution():
    eastern_segments = 6
    western_segments = 8

    # Calculate the difference in the number of segments
    segment_difference = western_segments - eastern_segments

    # Calculate the percentage difference
    percentage_difference = (segment_difference / western_segments) * 100

    result = percentage_difference
    return result

print(solution())