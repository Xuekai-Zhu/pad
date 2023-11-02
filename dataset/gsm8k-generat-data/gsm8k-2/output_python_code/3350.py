def solution():
    """Jefferson hires a carriage to go to the church. It is 20 miles away. The horse can go 10 miles per hour. It cost $30 per hour plus a flat fee of $20. How much did he pay for the carriage?"""
    distance = 20
    speed = 10
    time = distance / speed
    flat_fee = 20
    hourly_rate = 30
    total_cost = flat_fee + (hourly_rate * time)
    result = total_cost
    return result

print(solution())