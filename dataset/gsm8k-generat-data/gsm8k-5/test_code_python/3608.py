def solution():
    bacon_sandwiches_office = 10  # Each local office ordered 10 bacon sandwiches
    bacon_sandwiches_group = 4  # Half of the group that arrived asked for 4 bacon sandwiches each
    total_bacon_sandwiches = 54  # The café made a total of 54 bacon sandwiches

    # Calculate the number of bacon sandwiches made for the local offices
    bacon_sandwiches_for_offices = 3 * bacon_sandwiches_office

    # Calculate the number of bacon sandwiches made for the group that arrived
    bacon_sandwiches_for_group = (total_bacon_sandwiches - bacon_sandwiches_for_offices) / 2

    # Calculate the number of customers in the group that arrived
    customers_in_group = bacon_sandwiches_for_group / bacon_sandwiches_group
    result = customers_in_group
    return result

print(solution())