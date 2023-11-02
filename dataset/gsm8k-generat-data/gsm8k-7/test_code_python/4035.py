def solution():
    num_pigs = 2
    feed_per_pig_per_day = 10
    num_days = 7

    # Calculate the total amount of feed needed for both pigs for one day
    total_feed_per_day = num_pigs * feed_per_pig_per_day

    # Calculate the total amount of feed needed for both pigs for one week
    total_feed_per_week = total_feed_per_day * num_days

    result = total_feed_per_week
    return result

print(solution())