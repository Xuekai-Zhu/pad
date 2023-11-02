def solution():
    
    drops_per_minute = 20
    drops_per_hour = drops_per_minute * 60
    total_drops = drops_per_hour * 2
    ml_per_100_drops = 5
    total_ml = (total_drops // 100) * ml_per_100_drops
    result = total_ml
    return result

print(solution())