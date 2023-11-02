def solution():
    # Calculate the number of bacon sandwiches ordered by local offices
    office_orders = 3 * 10

    # Calculate the number of bacon sandwiches ordered by half of the group
    arrived_customers = (54 - office_orders) / 2
    group_size = arrived_customers / 4
    result = group_size
    return result

print(solution())