def solution():
    """Candace decides to enter a race. The race is run in 4 segments, with racers eliminated at the end of each segment. 10 racers are eliminated after the first segment. A third of the remaining racers are eliminated after the next section. Half of the remaining racers are eliminated before the last leg of the race. If 100 racers started the race, how many will run in the final section of the race?"""
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