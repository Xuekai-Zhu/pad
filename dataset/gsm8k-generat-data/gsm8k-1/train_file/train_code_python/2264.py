def solution():
    """There were 50 racers in a bicycle charity race at the beginning of the race. After 20 minutes, 30 more racers joined the race. The total number of racers doubled after another 30 minutes. If at the end of the race only 130 people finished the race, what's the total number of people who dropped before finishing the race?"""
    initial_racers = 50
    racers_joined = 30
    total_racers_20_min = initial_racers + racers_joined
    total_racers_50_min = total_racers_20_min * 2
    racers_dropped = total_racers_50_min - 130
    result = racers_dropped
    return result

print(solution())