def solution():
    """Randy feeds his pigs 10 pounds of feed per pig per day. If Randy has 2 pigs, how many pounds of pig feed will Randy's pigs be fed per week?"""
    # Define the number of pigs and pounds of feed per pig per day
    num_pigs = 2
    feed_per_pig_per_day = 10

    # Calculate the total pounds of feed per day
    total_feed_per_day = num_pigs * feed_per_pig_per_day

    # Calculate the total pounds of feed per week
    total_feed_per_week = total_feed_per_day * 7

    # return the result
    result = total_feed_per_week
    return result

print(solution())