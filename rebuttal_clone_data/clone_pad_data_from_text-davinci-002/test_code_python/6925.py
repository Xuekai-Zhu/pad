def solution():
    
    drops_per_minute = 20
    minutes_per_hour = 60
    hours_of_treatment = 2
    total_drops = drops_per_minute * minutes_per_hour * hours_of_treatment
    ml_per_100_drops = 5
    total_ml = total_drops * ml_per_100_drops / 100
    result = total_ml
    
    return result

print(solution())