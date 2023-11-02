def solution():
    # Calculate the cost of a single issue and the discounted cost of a single issue for the promotional subscription
    single_issue_cost = 34/(18*2)  # 18 months, twice-a-month issue
    discounted_issue_cost = single_issue_cost - 0.25

    # Calculate the total cost of the normal subscription and the promotional subscription
    normal_subscription_cost = 34
    promotional_subscription_cost = discounted_issue_cost * 18 * 2

    # Calculate the difference in cost between the normal subscription and the promotional subscription
    cost_difference = normal_subscription_cost - promotional_subscription_cost
    result = cost_difference
    return result

print(solution())