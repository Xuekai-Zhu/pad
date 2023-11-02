def solution():
    """Randy feeds his pigs 10 pounds of feed per pig per day. If Randy has 2 pigs, how many pounds of pig feed will Randy's pigs be fed per week?"""
    pounds_of_feed_per_day = 10
    number_of_pigs = 2
    days_per_week = 7
    total_pounds_of_feed = pounds_of_feed_per_day * number_of_pigs * days_per_week
    result = total_pounds_of_feed
    return result

print(solution())