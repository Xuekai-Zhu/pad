def solution():
    """Randy feeds his pigs 10 pounds of feed per pig per day. If Randy has 2 pigs, how many pounds of pig feed will Randy's pigs be fed per week?"""
    feed_per_pig_per_day = 10
    num_pigs = 2
    feed_per_week = feed_per_pig_per_day * num_pigs * 7
    result = feed_per_week
    return result

print(solution())