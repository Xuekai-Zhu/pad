def solution():
    
    piano_time = 20
    violin_time = 3 * piano_time
    days_per_week = 6
    weeks_per_month = 4
    total_time = (piano_time + violin_time) * days_per_week * weeks_per_month
    result = total_time
    return result

print(solution())