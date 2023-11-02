def solution():
    """Dexter has five pigs. Each one eats 4 pounds of feed, twice a day. If Dexter ordered 300 pounds of feed, how many pounds of feed is left after a week?"""
    pigs = 5
    feed_per_pig_per_day = 4 * 2
    days_per_week = 7
    total_feed = pigs * feed_per_pig_per_day * days_per_week
    feed_left = 300 - total_feed
    result = feed_left
    return result

print(solution())