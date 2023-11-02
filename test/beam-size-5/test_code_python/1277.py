def solution():
    num_pigs = 5
    feed_per_pig_per_day = 4
    num_days = 7
    total_feed_per_day = feed_per_pig_per_day * num_pigs * feed_per_pig_per_day
    total_feed_per_week = total_feed_per_day * num_days
    feed_left = 300 - total_feed_per_week
    result = feed_left
    return result

print(solution())