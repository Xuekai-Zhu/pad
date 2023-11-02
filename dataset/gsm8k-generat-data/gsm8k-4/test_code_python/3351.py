def solution():
    """Jefferson hires a carriage to go to the church. It is 20 miles away. The horse can go 10 miles per hour. It cost $30 per hour plus a flat fee of $20. How much did he pay for the carriage?"""
    # Define the distance and speed parameters
    distance = 20
    speed = 10

    # Calculate the time it takes to travel the distance
    time = distance / speed

    # Calculate the hourly cost and the total cost
    hourly_cost = 30
    flat_fee = 20
    total_cost = (hourly_cost * time) + flat_fee

    # return the result
    result = total_cost
    return result

print(solution())