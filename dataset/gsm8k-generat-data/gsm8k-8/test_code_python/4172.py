def solution():
    # Define the number of adults and children
    num_adults = 9
    num_children = 7

    # Define the cost of adult and children tickets
    adult_ticket_cost = 11
    child_ticket_cost = 7

    # Calculate the total cost of adult and children tickets
    total_adult_cost = num_adults * adult_ticket_cost
    total_child_cost = num_children * child_ticket_cost

    # Calculate the difference in cost
    difference = total_adult_cost - total_child_cost
    result = difference
    return result

print(solution())