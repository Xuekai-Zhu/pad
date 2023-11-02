def solution():
    """Andy is checking to see if all the cars in the parking lot paid for their parking. 75% of the cars have valid tickets, and 1/5th that number have permanent parking passes. If there are 300 cars in the parking lot, how many people tried to park in the lot without paying?"""
    total_cars = 300
    valid_tickets = int(total_cars * 0.75)
    permanent_passes = int(valid_tickets * 0.2)
    cars_without_payment = total_cars - valid_tickets - permanent_passes
    result = cars_without_payment
    return result

print(solution())