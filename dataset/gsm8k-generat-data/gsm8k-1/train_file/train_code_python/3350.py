def solution():
    """Jefferson hires a carriage to go to the church. It is 20 miles away. The horse can go 10 miles per hour. It cost $30 per hour plus a flat fee of $20. How much did he pay for the carriage?"""
    distance = 20
    speed = 10
    time = distance / speed
    hourly_fee = 30
    flat_fee = 20
    total_fee = time * hourly_fee + flat_fee
    result = total_fee
    return result

print(solution())