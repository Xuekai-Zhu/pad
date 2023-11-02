def solution():
    # Calculate the cost of the clown
    clown_cost = 100 * 4

    # Calculate the cost per hour of the bounce house
    bounce_house_hourly_cost = 3 * 100

    # Calculate the total cost of renting the bounce house for half the time
    bounce_house_cost = bounce_house_hourly_cost * 2

    # Calculate the total cost of the party
    total_cost = clown_cost + bounce_house_cost + 1000
    result = total_cost
    return result

print(solution())