def solution():
    
    caleb_bucket = 7
    cynthia_bucket = 8
    pool_capacity = 105
    combined_capacity = caleb_bucket + cynthia_bucket
    trips_needed = pool_capacity // combined_capacity
    if pool_capacity % combined_capacity > 0:
        trips_needed += 1
    result = trips_needed
    return result

print(solution())