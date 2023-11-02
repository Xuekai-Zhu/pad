def solution():
    # Define the number of adults, children, and senior citizens
    num_adults = 2
    num_children = 3
    num_seniors = 2

    # Calculate the total cost for the adults
    adult_cost = num_adults * 30

    # Calculate the total cost for the children
    children_cost = num_children * 15

    # Calculate the total cost for the senior citizens
    senior_cost = num_seniors * 0.9 * 30

    # Calculate the total cost for the entire family
    total_cost = adult_cost + children_cost + senior_cost
    result = total_cost
    return result

print(solution())