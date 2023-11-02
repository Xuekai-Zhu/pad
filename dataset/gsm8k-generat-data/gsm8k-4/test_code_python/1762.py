def solution():
    """Andy is checking to see if all the cars in the parking lot paid for their parking. 75% of the cars have valid tickets, and 1/5th that number have permanent parking passes. If there are 300 cars in the parking lot, how many people tried to park in the lot without paying?"""
    # Define the total number of cars in the parking lot
    total_cars = 300

    # Calculate the number of cars with valid tickets
    ticket_cars = total_cars * 0.75

    # Calculate the number of cars with permanent parking passes
    pass_cars = ticket_cars * (1/5)

    # Calculate the number of cars without valid tickets or passes
    unpaid_cars = total_cars - ticket_cars - pass_cars

    # Multiply the number of unpaid cars by the average number of people per car (assumed to be 1.5)
    unpaid_people = unpaid_cars * 1.5

    # return the result
    result = unpaid_people
    return result

print(solution())