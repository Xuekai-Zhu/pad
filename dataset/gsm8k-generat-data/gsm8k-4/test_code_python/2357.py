def solution():
    """Tim had a birthday party with a clown that cost $100 an hour for 4 hours.
    He also rented a bounce house for half the time that cost 3 times as much an hour.
    Everything else for the party cost $1000.
    How much did his birthday cost?"""
    # Define the cost of the clown and the duration
    clown_cost = 100 * 4

    # Define the cost per hour and duration of the bounce house
    bounce_cost_per_hour = 100 * 3
    bounce_duration = 4 / 2

    # Calculate the total cost of the bounce house
    bounce_cost = bounce_cost_per_hour * bounce_duration

    # Calculate the total cost of the party
    total_cost = clown_cost + bounce_cost + 1000

    # Return the result
    result = total_cost
    return result

print(solution())