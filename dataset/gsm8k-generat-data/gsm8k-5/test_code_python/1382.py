def solution():
    subscription_cost = 14  # The subscription costs $14 per month
    months = 12  # We want to know the cost after 1 year, which is 12 months

    # Calculate the total cost for the year
    total_cost = subscription_cost * months

    # Split the cost evenly with your friend
    cost_per_person = total_cost / 2
    result = cost_per_person
    return result

print(solution())