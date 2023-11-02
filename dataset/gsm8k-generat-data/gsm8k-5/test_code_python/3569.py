def solution():
    # Starting with 6000 liters
    liters = 6000
    
    # Evaporated 2000 liters
    liters -= 2000
    
    # Drained 3500 liters
    liters -= 3500
    
    # Rains for 30 minutes
    for i in range(3):
        # 350 liters of rain added every 10 minutes
        liters += 350
        
    result = liters
    return result

print(solution())