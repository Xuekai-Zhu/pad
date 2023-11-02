def solution():
    num_local_offices = 3
    num_bacon_sandwiches_per_local_office = 10
    num_bacon_sandwiches_per_customer_in_group = 4
    total_num_bacon_sandwiches = 54

    # Calculate the total number of bacon sandwiches ordered by local offices
    total_num_local_office_bacon_sandwiches = num_local_offices * num_bacon_sandwiches_per_local_office

    # Calculate the total number of bacon sandwiches ordered by the group of customers
    total_num_group_bacon_sandwiches = total_num_bacon_sandwiches - total_num_local_office_bacon_sandwiches

    # Calculate the number of customers in the group based on the total number of group bacon sandwiches
    num_customers_in_group = total_num_group_bacon_sandwiches / (num_bacon_sandwiches_per_customer_in_group / 2)
    result = num_customers_in_group
    return result

print(solution())