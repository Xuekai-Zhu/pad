def solution():
    """Andy is checking to see if all the cars in the parking lot paid for their parking. 75% of the cars have valid tickets, and 1/5th that number have permanent parking passes. If there are 300 cars in the parking lot, how many people tried to park in the lot without paying?"""
    # Find the number of cars with valid tickets
    valid_tickets = 0.75 * 300

    # Find the number of cars with permanent parking passes
    parking_passes = valid_tickets / 5

    # Find the number of cars without valid tickets or parking passes
    cars_without_payment = 300 - (valid_tickets + parking_passes)

    # Find the number of people who tried to park without paying
    people_without_payment = cars_without_payment * 4

    # Display the number of people without payment
    result = people_without_payment
    return result

print(solution())