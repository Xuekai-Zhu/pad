def solution():
    # Wages of 15 workers for 6 days
    wages_15_6 = 9450
    
    # Calculate the wages per worker per day
    wages_per_worker_per_day = wages_15_6 / (15*6)
    
    # Wages for 19 workers for 5 days
    wages_19_5 = wages_per_worker_per_day * (19*5)
    result = wages_19_5
    return result

print(solution())