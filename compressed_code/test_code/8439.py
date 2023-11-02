def solution():
    
    distance = 20
    speed = 10
    time = distance / speed
    hourly_fee = 30
    flat_fee = 20
    total_fee = time * hourly_fee + flat_fee
    result = total_fee
    return result

print(solution())