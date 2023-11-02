def solution():
    total_pizzas = 12  # The pizza delivery person has 12 pizzas to deliver
    multi_pizza_stops = 2  # There are 2 stops for orders of 2 pizzas each
    single_pizza_stops = total_pizzas - multi_pizza_stops  # The remaining stops are for single pizzas
    total_stops = multi_pizza_stops + single_pizza_stops  # The total number of stops is the sum of the multi-pizza stops and single-pizza stops
    total_time = 40  # The pizza delivery person has 40 minutes to deliver all of the pizzas

    # Calculate the average time per stop
    average_time_per_stop = (total_time / total_stops)

    result = average_time_per_stop
    return result

print(solution())