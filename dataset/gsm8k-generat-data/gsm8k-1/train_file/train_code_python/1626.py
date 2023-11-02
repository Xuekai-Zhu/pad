def solution():
    """Grace is filling her pool in the backyard with a hose that sprays 50 gallons/hour. She waited for 3 hours but the pool wasn't full, so she decides to add another hose that sprays 70 gallons/hour, and after 2 more hours the pool is full. How much water can Grace’s pool contain?"""
    first_hose_rate = 50
    second_hose_rate = 70
    first_hose_time = 3
    second_hose_time = 2
    total_time = first_hose_time + second_hose_time
    total_gallons_filled = (first_hose_rate * first_hose_time) + (second_hose_rate * second_hose_time)
    pool_capacity = total_gallons_filled / total_time
    result = pool_capacity
    return result

print(solution())