def solution():
    # Define variables
    normal_cost = 34
    discount_per_issue = 0.25
    issues_per_month = 2
    subscription_length = 18  # months
    
    # Calculate number of issues and total cost for normal subscription
    total_issues_normal = issues_per_month * subscription_length
    total_cost_normal = total_issues_normal * normal_cost
    
    # Calculate number of issues and total cost for promotional subscription
    total_issues_promo = total_issues_normal
    total_cost_promo = total_issues_promo * (normal_cost - discount_per_issue)
    
    # Calculate the difference in cost and return the result
    cost_difference = total_cost_normal - total_cost_promo
    return cost_difference

print(solution())