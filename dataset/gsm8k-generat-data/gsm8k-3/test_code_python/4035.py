def solution():
    """Randy feeds his pigs 10 pounds of feed per pig per day.  If Randy has 2 pigs, how many pounds of pig feed will Randy's pigs be fed per week?"""
    # Define the feed amount per pig per day and the number of pigs Randy has
    feed_per_pig_per_day = 10
    num_pigs = 2

    # Calculate the total feed required for one pig for a week
    feed_per_pig_per_week = feed_per_pig_per_day * 7

    # Calculate the total feed required for all pigs for a week
    total_feed_per_week = feed_per_pig_per_week * num_pigs

    # Display the total feed required
    result = total_feed_per_week
    return result

print(solution())