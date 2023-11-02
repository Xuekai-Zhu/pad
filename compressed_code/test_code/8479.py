def solution():
    
    num_shirts = 10
    num_pants = 12
    shirt_time = 1.5
    pant_time = 2 * shirt_time
    hourly_rate = 30
    total_time = num_shirts * shirt_time + num_pants * pant_time
    total_cost = total_time * hourly_rate
    result = total_cost
    return result

print(solution())