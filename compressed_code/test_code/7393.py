def solution():
    
    total_time = 8 * 60  
    train_time = 6 * 60  
    wait_time = 15 * 2  
    bus_time = total_time - train_time - wait_time - 15  
    result = bus_time
    return result

print(solution())