def solution():
    distance = 20
    speed = 10
    flat_fee = 20
    hourly_rate = 30

    # Calculate the time it takes to travel to the church
    time = distance / speed

    # Round up to the nearest hour
    time = math.ceil(time)

    # Calculate the total cost of the carriage ride
    total_cost = (time * hourly_rate) + flat_fee
    result = total_cost
    return result

print(solution())