def solution():
    total_cars = 300  # Total number of cars in the parking lot
    valid_tickets = 0.75 * total_cars  # Number of cars with valid tickets
    permanent_passes = 0.2 * valid_tickets  # Number of cars with permanent parking passes
    paid_cars = valid_tickets + permanent_passes  # Total number of cars that paid for parking

    # Calculate the number of cars that did not pay for parking
    unpaid_cars = total_cars - paid_cars
    result = unpaid_cars
    return result

print(solution())