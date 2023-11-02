def solution():
    """The pizza delivery person has 12 pizzas to deliver. If two of the stops are for orders of two pizzas and the rest are for single pizzas, how many minutes per stop does the delivery person need to average to deliver all of the pizzas in 40 minutes?"""
    total_pizzas = 12
    double_orders = 2
    single_orders = total_pizzas - double_orders
    total_stops = single_orders + double_orders
    total_time = 40
    time_per_single = total_time / single_orders
    time_per_double = time_per_single * 2
    average_time = (time_per_single * single_orders + time_per_double * double_orders) / total_stops
    result = average_time
    return result

print(solution())