def solution():
    total_racers = 100  # 100 racers started the race
    eliminated_segment_1 = 10  # 10 racers are eliminated after the first segment
    remaining_racers_1 = total_racers - eliminated_segment_1  # Racers remaining after first segment
    eliminated_segment_2 = remaining_racers_1 // 3  # A third of remaining racers are eliminated after the second segment
    remaining_racers_2 = remaining_racers_1 - eliminated_segment_2  # Racers remaining after second segment
    eliminated_segment_3 = remaining_racers_2 // 2  # Half of remaining racers are eliminated before the last leg
    remaining_racers_3 = remaining_racers_2 - eliminated_segment_3  # Racers remaining for the last section of the race
    result = remaining_racers_3
    return result

print(solution())