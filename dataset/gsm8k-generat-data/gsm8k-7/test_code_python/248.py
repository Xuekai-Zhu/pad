def solution():
    normal_subscription_price = 34
    discount_per_issue = 0.25
    num_issues = 18 * 2

    # Calculate the discount for each issue
    total_discount = discount_per_issue * num_issues

    # Calculate the promotional subscription price
    promotional_price = normal_subscription_price - total_discount

    # Calculate the difference between the two prices
    price_difference = normal_subscription_price - promotional_price
    result = price_difference
    return result

print(solution())