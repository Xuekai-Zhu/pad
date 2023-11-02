def solution():
    drops_per_minute = 20
    minutes = 120  # 2 hours
    drops_per_hour = drops_per_minute * 60
    total_drops = drops_per_hour * minutes

    ml_per_100_drops = 5
    ml_per_drop = ml_per_100_drops / 100

    total_ml = total_drops * ml_per_drop
    result = total_ml
    return result

print(solution())