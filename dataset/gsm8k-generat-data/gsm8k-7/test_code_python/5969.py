def solution():
    start_racers = 100
    eliminated_segment_1 = 10
    eliminated_segment_2 = (start_racers - eliminated_segment_1) / 3
    remaining_after_segment_2 = start_racers - eliminated_segment_1 - eliminated_segment_2
    eliminated_segment_3 = remaining_after_segment_2 / 2
    final_racers = remaining_after_segment_2 - eliminated_segment_3
    result = final_racers
    return result

print(solution())