def solution():
    regular_customers_per_hour = 175
    holiday_customers_per_hour = regular_customers_per_hour * 2
    num_hours = 8

    # Calculate the total number of customers during the holiday season
    total_customers = holiday_customers_per_hour * num_hours
    result = total_customers
    return result

print(solution())