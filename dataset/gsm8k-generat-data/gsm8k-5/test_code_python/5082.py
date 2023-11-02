def solution():
    # Calculate the money made from commercial views
    commercial_money = 0.50 * 100  # Lauren had 100 views on Tuesday

    # Calculate the money made from subscriptions
    subscription_money = 1.00 * 27  # 27 people subscribed on Tuesday

    # Calculate the total money made on Tuesday
    total_money = commercial_money + subscription_money
    result = total_money
    return result

print(solution())