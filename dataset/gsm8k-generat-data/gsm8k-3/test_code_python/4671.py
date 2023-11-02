def solution():
    """The pizza delivery person has 12 pizzas to deliver.  If two of the stops are for orders of two pizzas and the rest are for single pizzas, how many minutes per stop does the delivery person need to average to deliver all of the pizzas in 40 minutes?"""
    # Define the number of pizzas and stops
    NUM_PIZZAS = 12
    NUM_STOPS = 10 # 2 stops for 2 pizzas, 8 stops for 1 pizza

    # Define the total time available for delivery
    TOTAL_TIME = 40 # in minutes

    # Calculate the average time per stop
    time_per_stop = (TOTAL_TIME - 2) / NUM_STOPS # subtract 2 minutes for the 2nd stop with 2 pizzas

    # Display the average time per stop
    result = time_per_stop
    return result

print(solution())