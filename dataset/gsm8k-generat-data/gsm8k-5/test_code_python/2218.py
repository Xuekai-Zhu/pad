def solution():
    east_tail_segments = 6
    west_tail_segments = 8
    difference_in_segments = west_tail_segments - east_tail_segments
    percentage_difference = (difference_in_segments / west_tail_segments) * 100
    result = percentage_difference
    return result

print(solution())