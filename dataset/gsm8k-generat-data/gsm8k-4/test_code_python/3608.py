def solution():
    """A café has a few orders to cook and also needs to makes sandwiches for a group of customers that arrived. 3 local offices have each ordered 10 bacon sandwiches and half of the group that has arrived have asked for 4 bacon sandwiches each. If the café makes a total of 54 bacon sandwiches, how many customers are in the group of customers that arrived?"""
    
    # Define the number of bacon sandwiches ordered by the local offices
    office_orders = 3 * 10

    # Define the total number of bacon sandwiches made
    total_orders = 54

    # Calculate the number of bacon sandwiches made for the group
    group_orders = total_orders - office_orders

    # Calculate the number of customers in the group
    group_customers = group_orders / 2 / 4

    result = group_customers
    return result

print(solution())