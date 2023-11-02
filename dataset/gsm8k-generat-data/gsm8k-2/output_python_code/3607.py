def solution():
    """A café has a few orders to cook and also needs to makes sandwiches for a group of customers that arrived. 3 local offices have each ordered 10 bacon sandwiches and half of the group that has arrived have asked for 4 bacon sandwiches each. If the café makes a total of 54 bacon sandwiches, how many customers are in the group of customers that arrived?"""
    office_orders = 3 * 10
    group_orders = (54 - office_orders) / 2
    group_size = group_orders / 4
    result = group_size
    return result

print(solution())