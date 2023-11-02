def solution():
    """The pizza delivery person has 12 pizzas to deliver. If two of the stops are for orders of two pizzas and the rest are for single pizzas, how many minutes per stop does the delivery person need to average to deliver all of the pizzas in 40 minutes?"""
    total_pizzas = 12
    double_orders = 2
    single_orders = total_pizzas - double_orders
    total_stops = single_orders + double_orders
    available_time = 40
    time_per_stop = (available_time * 60) / total_stops
    result = time_per_stop
    return result

print(solution())