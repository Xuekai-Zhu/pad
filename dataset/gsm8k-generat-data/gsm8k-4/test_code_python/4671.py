def solution():
    """The pizza delivery person has 12 pizzas to deliver. If two of the stops are for orders of two pizzas and the rest are for single pizzas, how many minutes per stop does the delivery person need to average to deliver all of the pizzas in 40 minutes?"""
    # Define the number of pizzas to deliver and the time available
    pizzas_to_deliver = 12
    available_time = 40

    # Define the time for the two double orders and subtract them from the available time
    double_orders_time = 2 * 10
    available_time -= double_orders_time

    # Calculate the remaining time per stop, assuming equal time for all single order stops
    single_order_time = available_time / (pizzas_to_deliver - 2)

    # Return the result
    result = single_order_time
    return result

print(solution())