def solution():
    """Tim had a birthday party with a clown that cost $100 an hour for 4 hours.  He also rented a bounce house for half the time that cost 3 times as much an hour. Everything else for the party cost $1000.  How much did his birthday cost?"""
    # Define the cost of the clown per hour and the number of hours
    CLOWN_COST = 100
    CLOWN_HOURS = 4

    # Define the cost of the bounce house per hour and the number of hours
    BOUNCE_HOUSE_COST = CLOWN_COST * 3
    BOUNCE_HOUSE_HOURS = CLOWN_HOURS / 2

    # Calculate the total cost of the clown and bounce house
    clown_cost = CLOWN_COST * CLOWN_HOURS
    bounce_house_cost = BOUNCE_HOUSE_COST * BOUNCE_HOUSE_HOURS
    total_cost = clown_cost + bounce_house_cost + 1000

    # Display the total cost
    result = total_cost
    return result

print(solution())