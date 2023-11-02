def solution():
    """An 18-month magazine subscription is normally $34. The magazine is currently running a promotion for $0.25 off each twice-a-month issue when signing up for the 18-month subscription. How many dollars cheaper is the promotional subscription than the normal one?"""
    # Define the normal price of the subscription
    normal_price = 34

    # Calculate the discounted price per issue
    discounted_price = 0.25

    # Calculate the number of issues in the 18-month subscription
    num_issues = 18 * 2

    # Calculate the total discount for the promotional subscription
    total_discount = discounted_price * num_issues

    # Calculate the final price of the promotional subscription
    promo_price = normal_price - total_discount

    # Calculate the difference between the normal and promotional prices
    price_difference = normal_price - promo_price

    # return the result
    result = price_difference
    return result

print(solution())