def solution():
    # Calculate the number of cars with valid tickets
    cars_with_tickets = 0.75 * 300

    # Calculate the number of cars with permanent parking passes
    cars_with_parking_passes = (1/5) * cars_with_tickets

    # Calculate the number of cars without valid tickets or parking passes
    cars_without_tickets_or_passes = 300 - cars_with_tickets - cars_with_parking_passes

    result = cars_without_tickets_or_passes
    return result

print(solution())