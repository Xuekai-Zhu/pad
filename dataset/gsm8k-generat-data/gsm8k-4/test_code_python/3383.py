def solution():
    """Hannah's AdBlock blocks all but 20% of ads, and 20% of the ads it doesn't block are actually interesting. What percentage of ads aren't interested and don't get blocked?"""
    # Define the percentage of ads blocked by AdBlock
    blocked_percent = 80

    # Calculate the percentage of ads that aren't blocked
    not_blocked_percent = 100 - blocked_percent

    # Calculate the percentage of not blocked ads that are not interesting
    not_interesting_percent = not_blocked_percent * 0.8

    # Calculate the percentage of ads that are not interesting and don't get blocked
    not_interesting_not_blocked = not_interesting_percent / 100 * blocked_percent

    # return the result
    result = not_interesting_not_blocked
    return result

print(solution())