def solution():
    """Lauren's social media channel makes $0.50 for every commercial that's viewed and $1.00 for every person who subscribes. On Tuesday, 100 people watched commercials before viewing her content and 27 people subscribed. How much money did she make?"""
    commercial_views = 100
    subscription_count = 27
    commercial_earnings = 0.5 * commercial_views
    subscription_earnings = 1 * subscription_count
    total_earnings = commercial_earnings + subscription_earnings
    result = total_earnings
    return result

print(solution())