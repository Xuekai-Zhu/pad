def solution():
    subscription_cost = 14.0
    num_people = 2  # splitting with a friend
    num_months = 12

    # Calculate the total cost per person for the year
    total_cost = subscription_cost * num_months
    cost_per_person = total_cost / num_people

    result = cost_per_person
    return result

print(solution())