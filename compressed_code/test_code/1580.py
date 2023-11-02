def solution():
    
    total_travel_time = 8*60 
    train_ride_time = 6*60 
    wait_time = 2*15 
    bus_walk_time = 15
    bus_ride_time = total_travel_time - train_ride_time - wait_time - bus_walk_time
    result = bus_ride_time
    return result

print(solution())