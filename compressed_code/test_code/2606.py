def solution():
    
    distance = 20
    speed = 10
    time = distance / speed
    flat_fee = 20
    hourly_rate = 30
    total_cost = flat_fee + (hourly_rate * time)
    result = total_cost
    return result

print(solution())