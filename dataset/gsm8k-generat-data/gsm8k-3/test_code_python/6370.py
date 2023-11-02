def solution():
    """A mechanic charges $60 an hour to repair a car.  He works 8 hours a day for 14 days on one car.  The mechanic also used $2500 in parts.  How much did the car's owner have to pay?"""
    # Define the hourly rate and number of hours worked
    HOURLY_RATE = 60
    HOURS_WORKED = 8 * 14

    # Calculate the total cost of labor
    labor_cost = HOURLY_RATE * HOURS_WORKED

    # Add the cost of parts
    total_cost = labor_cost + 2500

    # Display the total cost
    result = total_cost
    return result

print(solution())