def solution():
    """Hannah's AdBlock blocks all but 20% of ads, and 20% of the ads it doesn't block are actually interesting. What percentage of ads aren't interested and don't get blocked?"""
    blocked_ads_percentage = 80
    interesting_ads_percentage = 20 * 0.2
    uninteresting_unblocked_ads_percentage = blocked_ads_percentage * (1 - interesting_ads_percentage / 100)
    result = uninteresting_unblocked_ads_percentage
    return result

print(solution())