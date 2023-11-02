def solution():
    drops_per_minute = 10
    milliliters_per_drop = 0.05
    minutes_in_one_hour = 60
    total_drops = drops_per_minute * minutes_in_one_hour
    total_milliliters = total_drops * milliliters_per_drop
    result = total_milliliters
    return result

print(solution())