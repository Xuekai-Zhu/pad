def solution():
    distance = 20  # The distance to the church is 20 miles
    speed = 10  # The horse can go 10 miles per hour
    time = distance / speed  # Calculate the time it takes to reach the church

    # Calculate the total cost of the carriage ride
    hourly_cost = 30  # The hourly cost of the carriage is $30
    flat_fee = 20  # The flat fee for the carriage is $20
    total_cost = hourly_cost * time + flat_fee

    result = total_cost
    return result

print(solution())