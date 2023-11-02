def solution():
    # Calculate the total cost of hiring the carriage
    distance = 20  # miles to the church
    speed = 10  # miles per hour
    time = distance / speed  # time taken to reach the church
    total_cost = time * 30 + 20  # $30 per hour plus a flat fee of $20
    result = total_cost
    return result

print(solution())