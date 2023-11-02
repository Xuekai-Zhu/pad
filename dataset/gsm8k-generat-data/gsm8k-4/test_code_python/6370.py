def solution():
    """A mechanic charges $60 an hour to repair a car. He works 8 hours a day for 14 days on one car. The mechanic also used $2500 in parts. How much did the car's owner have to pay?"""
    # Define the hourly rate and number of working days
    hourly_rate = 60
    working_days = 14

    # Calculate the total number of hours worked
    total_hours = 8 * working_days

    # Calculate the total cost of labor
    labor_cost = hourly_rate * total_hours

    # Add the cost of parts
    total_cost = labor_cost + 2500

    result = total_cost
    return result

print(solution())