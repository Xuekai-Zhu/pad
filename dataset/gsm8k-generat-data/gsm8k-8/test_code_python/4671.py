def solution():
    # Calculate the number of single pizza orders
    single_orders = 12 - 2*2

    # Calculate the total time for pizza deliveries
    total_time = 40

    # Calculate the time for the two double orders
    double_order_time = 2 * 10

    # Calculate the remaining time for single orders
    remaining_time = total_time - double_order_time

    # Calculate the time per single order
    time_per_order = remaining_time / single_orders

    result = time_per_order
    return result

print(solution())