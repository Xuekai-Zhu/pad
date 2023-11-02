def solution():
    piano_time = 20 # minutes per day
    violin_time = 3 * piano_time # three times longer than piano

    num_days = 6 # days per week
    num_weeks = 4 # weeks in a month

    total_practice_time = (piano_time + violin_time) * num_days * num_weeks
    result = total_practice_time
    return result

print(solution())