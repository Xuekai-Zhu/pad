def solution():
    total_sandwiches = 54
    office_orders = 3 * 10
    customer_orders = (total_sandwiches - office_orders) / 4
    result = customer_orders
    return result

print(solution())