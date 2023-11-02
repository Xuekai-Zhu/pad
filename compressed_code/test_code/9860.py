def solution():
    
    total_homes = 200
    homes_distributed_first_hour = 2/5 * total_homes
    homes_remaining = total_homes - homes_distributed_first_hour
    homes_distributed_second_hour = 0.6 * homes_remaining
    homes_left = homes_remaining - homes_distributed_second_hour
    result = homes_left
    return result

print(solution())