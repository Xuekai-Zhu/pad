def solution():
    # Calculate the number of stops and pizzas per stop for the single pizza orders
    single_pizza_stops = 12 - 2  # 2 of the stops are for orders of 2 pizzas
    single_pizzas_per_stop = 1

    # Calculate the number of stops and pizzas per stop for the double pizza orders
    double_pizza_stops = 2
    double_pizzas_per_stop = 2

    # Calculate the total number of pizzas and stops
    total_pizzas = single_pizza_stops * single_pizzas_per_stop + double_pizza_stops * double_pizzas_per_stop
    total_stops = single_pizza_stops + double_pizza_stops

    # Calculate the average time per stop
    average_time_per_stop = 40 / total_stops

    # Round the result to the nearest minute
    result = round(average_time_per_stop)
    return result

print(solution())