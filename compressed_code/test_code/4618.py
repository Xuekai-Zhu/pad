def solution():
    
    starting_racers = 100
    eliminated_after_first = 10
    remaining_racers_1 = starting_racers - eliminated_after_first
    eliminated_after_second = remaining_racers_1 / 3
    remaining_racers_2 = remaining_racers_1 - eliminated_after_second
    eliminated_before_last = remaining_racers_2 / 2
    remaining_racers_3 = remaining_racers_2 - eliminated_before_last
    result = remaining_racers_3
    return result

print(solution())