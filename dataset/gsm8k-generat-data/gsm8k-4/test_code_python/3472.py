def solution():
    """Tom rents a helicopter for 2 hours a day for 3 days. It cost $75 an hour to rent. How much did he pay?"""
    # Define the rental cost of the helicopter per hour
    rental_cost = 75

    # Define the number of hours Tom rented the helicopter per day and for how many days
    hours_per_day = 2
    days = 3

    # Calculate the total cost of renting the helicopter
    total_cost = rental_cost * hours_per_day * days

    result = total_cost
    return result

print(solution())