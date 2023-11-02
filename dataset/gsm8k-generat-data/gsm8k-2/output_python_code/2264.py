def solution():
    """There were 50 racers in a bicycle charity race at the beginning of the race. After 20 minutes, 30 more racers joined the race. The total number of racers doubled after another 30 minutes. If at the end of the race only 130 people finished the race, what's the total number of people who dropped before finishing the race?"""
    initial_racers = 50
    new_racers_after_20_minutes = 30
    total_racers_after_20_minutes = initial_racers + new_racers_after_20_minutes
    total_racers_after_50_minutes = total_racers_after_20_minutes * 2
    racers_who_finished = 130
    racers_who_dropped = total_racers_after_50_minutes - racers_who_finished
    result = racers_who_dropped
    return result

print(solution())