def solution():
    # Define the variables
    subscription_cost = 14
    months_in_year = 12
    num_people = 2

    # Calculate the total cost for one year
    total_cost = subscription_cost * months_in_year

    # Calculate the cost per person for one year
    cost_per_person = total_cost / num_people

    # Return the total cost per person for one year
    result = cost_per_person
    return result

print(solution())