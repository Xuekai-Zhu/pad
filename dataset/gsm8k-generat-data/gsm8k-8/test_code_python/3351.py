def solution():
    distance = 20
    speed = 10
    time = distance / speed
    hourly_rate = 30
    flat_fee = 20
    total_cost = time * hourly_rate + flat_fee
    result = total_cost
    return result

print(solution())