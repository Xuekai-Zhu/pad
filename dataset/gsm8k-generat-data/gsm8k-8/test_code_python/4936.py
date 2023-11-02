def solution():
    # Initialize the buckets
    bucket3 = 0
    bucket5 = 5
    bucket6 = 0
    
    # Pour from the 5-liter to the 3-liter bucket
    bucket3 = min(bucket5, 3)
    bucket5 -= bucket3
    
    # Pour the remaining water into the 6-liter bucket
    bucket6 += bucket5
    
    # Calculate how much more water can be added to the 6-liter bucket
    max_capacity = 6
    current_volume = bucket6
    remaining_capacity = max_capacity - current_volume
    result = remaining_capacity
    return result

print(solution())