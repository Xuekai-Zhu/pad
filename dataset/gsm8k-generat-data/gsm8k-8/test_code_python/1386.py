def solution():
    # Calculate the total number of cars
    total_cars = 4 + 6

    # Calculate the total number of tires needed
    total_tires = 4 * 4 + 6 * 4

    # Calculate the number of tires not needed
    tires_not_needed = 2 * 2

    # Calculate the number of tires left after all changes
    tires_left = 20

    # Calculate the number of customers who did not want their tires changing
    customers_no_change = (tires_left + tires_not_needed - total_tires) / 4

    result = customers_no_change
    return result

print(solution())