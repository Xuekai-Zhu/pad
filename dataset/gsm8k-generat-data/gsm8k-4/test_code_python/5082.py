def solution():
    """Lauren's social media channel makes $0.50 for every commercial that's viewed and $1.00 for every person who subscribes. On Tuesday, 100 people watched commercials before viewing her content and 27 people subscribed. How much money did she make?"""
    # Define the revenue from commercials and subscriptions
    commercial_revenue = 0.5 * 100
    subscription_revenue = 1.0 * 27

    # Calculate the total revenue
    total_revenue = commercial_revenue + subscription_revenue

    # Return the result
    result = total_revenue
    return result

print(solution())