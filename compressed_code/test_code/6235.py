def solution():
    
    cherries_needed = 3 * 80
    cherries_pitted_per_round = 20
    minutes_per_round = 10
    rounds_needed = cherries_needed // cherries_pitted_per_round
    total_minutes = rounds_needed * minutes_per_round
    hours_needed = total_minutes / 60
    result = hours_needed
    return result

print(solution())