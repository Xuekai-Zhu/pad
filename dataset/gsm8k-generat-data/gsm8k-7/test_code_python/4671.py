def solution():
    total_pizzas = 12
    double_stops = 2
    single_stops = total_pizzas - double_stops
    time_limit = 40  # minutes

    # Calculate the remaining time after delivering the two double stops
    remaining_time = time_limit - (2 * 10)  # each double stop takes 10 minutes

    # Calculate the average time per stop for the rest of the orders
    avg_time = remaining_time / single_stops
    result = avg_time
    return result

print(solution())