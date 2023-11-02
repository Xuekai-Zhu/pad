def solution():
    
    uber_cost = 22
    lyft_cost = uber_cost - 3
    taxi_cost = lyft_cost - 4
    tip_percentage = 0.2
    taxi_tip = taxi_cost * tip_percentage
    total_cost = taxi_cost + taxi_tip
    result = total_cost
    return result

print(solution())