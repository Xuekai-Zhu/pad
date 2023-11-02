def solution():
    body_segments_needed = 800
    body_segments_eaten = 60 + (2 * 2 * 60)  # 2 millipedes that are twice as long
    body_segments_still_needed = body_segments_needed - body_segments_eaten
    num_50_segment_millipedes_needed = body_segments_still_needed / 50
    result = num_50_segment_millipedes_needed
    return result

print(solution())