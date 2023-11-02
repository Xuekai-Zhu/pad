def solution():
    """A café has a few orders to cook and also needs to makes sandwiches for a group of customers that arrived. 3 local offices have each ordered 10 bacon sandwiches and half of the group that has arrived have asked for 4 bacon sandwiches each. If the café makes a total of 54 bacon sandwiches, how many customers are in the group of customers that arrived?"""
    # Define the number of bacon sandwiches ordered by each office
    OFFICE_ORDER = 10

    # Calculate the total number of bacon sandwiches ordered by the offices
    office_total = OFFICE_ORDER * 3

    # Calculate the total number of bacon sandwiches requested by the group
    group_requested = (54 - office_total) / 2

    # Calculate the number of customers in the group
    customers = group_requested / 4

    # Display the number of customers in the group
    result = customers
    return result

print(solution())