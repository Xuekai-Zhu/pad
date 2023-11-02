def solution():
    total_days = 30  # Frank has 30 days to meet his quota
    total_cars_needed = 50  # Frank needs to sell 50 cars in 30 days

    # Calculate the total cars Frank has sold in the first 7 days
    cars_sold_first_week = 5 * 3 + 3 * 4  # Frank sold 5 cars each for the first 3 days and 3 cars each for the next 4 days

    # Calculate the remaining days and the remaining cars Frank needs to sell
    remaining_days = total_days - 7
    remaining_cars_needed = total_cars_needed - cars_sold_first_week

    # Calculate the average number of cars Frank needs to sell per day to meet his quota
    average_cars_per_day = remaining_cars_needed / remaining_days

    result = average_cars_per_day
    return result

print(solution())