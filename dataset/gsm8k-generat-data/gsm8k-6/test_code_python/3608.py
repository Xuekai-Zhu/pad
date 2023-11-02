def solution():
    # Calculate the number of bacon sandwiches needed for the local offices and subtract it from the total
    num_office_sandwiches = 3 * 10  # each office ordered 10 bacon sandwiches
    num_group_sandwiches = 54 - num_office_sandwiches  
    # the total number of sandwiches needed for the group is the difference between total and office sandwiches

    # Calculate the number of customers in the group
    num_group_customers = num_group_sandwiches // 4  # each customer in the group ordered 4 sandwiches
    result = num_group_customers
    return result

print(solution())