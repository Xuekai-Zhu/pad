def solution():
    """An 18-month magazine subscription is normally $34. The magazine is currently running a promotion for $0.25 off each twice-a-month issue when signing up for the 18-month subscription. How many dollars cheaper is the promotional subscription than the normal one?"""
    # Define the cost of a normal 18-month subscription and the discount per issue for the promotional subscription
    NORMAL_COST = 34
    PROMOTIONAL_DISCOUNT = 0.25

    # Calculate the number of issues over the 18-month subscription
    num_issues = 18 * 2

    # Calculate the cost of the promotional subscription
    promotional_cost = NORMAL_COST - (num_issues * PROMOTIONAL_DISCOUNT)

    # Calculate the difference between the promotional and normal subscriptions
    cost_difference = NORMAL_COST - promotional_cost

    # Display the cost difference
    result = cost_difference
    return result

print(solution())