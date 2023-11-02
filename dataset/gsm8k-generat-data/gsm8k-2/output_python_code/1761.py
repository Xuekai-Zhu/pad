def solution():
    """Andy is checking to see if all the cars in the parking lot paid for their parking. 75% of the cars have valid tickets, and 1/5th that number have permanent parking passes. If there are 300 cars in the parking lot, how many people tried to park in the lot without paying?"""
    total_cars = 300
    valid_tickets = 0.75 * total_cars
    permanent_passes = valid_tickets / 5
    unpaid_cars = total_cars - (valid_tickets + permanent_passes)
    result = unpaid_cars
    return result

print(solution())