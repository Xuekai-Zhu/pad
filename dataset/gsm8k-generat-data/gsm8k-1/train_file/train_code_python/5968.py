def solution():
    """Candace decides to enter a race. The race is run in 4 segments, with racers eliminated at the end of each segment. 10 racers are eliminated after the first segment. 
    A third of the remaining racers are eliminated after the next section. Half of the remaining racers are eliminated before the last leg of the race. 
    If 100 racers started the race, how many will run in the final section of the race?"""
    
    total_racers = 100
    racers_eliminated_segment_1 = 10
    remaining_racers_segment_1 = total_racers - racers_eliminated_segment_1
    racers_eliminated_segment_2 = remaining_racers_segment_1 // 3
    remaining_racers_segment_2 = remaining_racers_segment_1 - racers_eliminated_segment_2
    racers_eliminated_segment_3 = remaining_racers_segment_2 // 2
    remaining_racers_segment_3 = remaining_racers_segment_2 - racers_eliminated_segment_3
    racers_in_final_segment = remaining_racers_segment_3
    
    result = racers_in_final_segment
    return result

print(solution())