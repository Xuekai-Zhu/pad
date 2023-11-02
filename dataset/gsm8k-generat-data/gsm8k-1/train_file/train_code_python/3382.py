def solution():
    """Hannah's AdBlock blocks all but 20% of ads, and 20% of the ads it doesn't block are actually interesting. What percentage of ads aren't interested and don't get blocked?"""
    ads_blocked = 0.8
    ads_not_blocked = 1 - ads_blocked
    interesting_ads = 0.2
    uninteresting_ads = ads_not_blocked - (ads_not_blocked * interesting_ads)
    result = uninteresting_ads * 100
    return result

print(solution())