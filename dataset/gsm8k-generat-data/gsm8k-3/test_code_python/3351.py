def solution():
    """Jefferson hires a carriage to go to the church.  It is 20 miles away.  The horse can go 10 miles per hour.  It cost $30 per hour plus a flat fee of $20.  How much did he pay for the carriage?"""
    # Define the distance and speed of the carriage
    distance = 20
    speed = 10

    # Calculate the time it takes to travel to the church
    time = distance / speed

    # Calculate the cost of the carriage
    cost = time * 30 + 20

    # Display the cost of the carriage
    result = cost
    return result

print(solution())