def solution():
    """Grace is filling her pool in the backyard with a hose that sprays 50 gallons/hour. She waited for 3 hours but the pool wasn't full, so she decides to add another hose that sprays 70 gallons/hour, and after 2 more hours the pool is full. How much water can Grace’s pool contain?"""
    # Define the initial filling rate and the additional filling rate
    RATE1 = 50
    RATE2 = 70
    
    # Calculate the amount of water added in the first 3 hours
    amount1 = RATE1 * 3
    
    # Calculate the remaining amount of water needed to fill the pool
    remaining_amount = 0.0
    
    if amount1 < 1.0:
        remaining_amount = 1.0
        
    remaining_amount += amount1/2
    
    # Calculate the total amount of water added
    total_amount = amount1 + remaining_amount
    
    # Calculate the pool capacity
    pool_capacity = total_amount/(RATE1 + RATE2)
    
    # Display the pool capacity
    result = pool_capacity
    return result

print(solution())