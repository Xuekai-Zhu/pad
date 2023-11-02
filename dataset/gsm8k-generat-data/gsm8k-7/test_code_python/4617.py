def solution():
    price_per_subscription = 5.0

    # Calculate the total number of subscriptions sold
    total_subscriptions = 4 + 1 + 2 + (2 * 2)

    # Calculate the total earnings from selling subscriptions
    total_earnings = total_subscriptions * price_per_subscription
    result = total_earnings
    return result

print(solution())