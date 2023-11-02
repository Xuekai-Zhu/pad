def solution():
    months = 18  # the subscription is for 18 months
    normal_price = 34  # the normal price for the subscription is $34
    discount = 0.25  # the promotional discount is $0.25 per issue
    issues = months * 2  # there are twice-a-month issues for the 18-month subscription

    # Calculate the total cost of the promotional subscription
    promotional_price = (normal_price - discount) * issues

    # Calculate the difference between the normal and promotional subscription
    difference = normal_price - promotional_price
    result = difference
    return result

print(solution())