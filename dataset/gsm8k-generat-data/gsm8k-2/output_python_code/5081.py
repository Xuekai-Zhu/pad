def solution():
    """Lauren's social media channel makes $0.50 for every commercial that's viewed and $1.00 for every person who subscribes. On Tuesday, 100 people watched commercials before viewing her content and 27 people subscribed. How much money did she make?"""
    commercial_payment = 0.5 * 100
    subscription_payment = 1 * 27
    total_payment = commercial_payment + subscription_payment
    result = total_payment
    return result

print(solution())