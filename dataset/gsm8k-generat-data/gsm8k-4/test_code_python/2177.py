def solution():
    """Toby, the Alaskan Malamute, can pull a sled at a speed of 20 miles per hour if the sled is unloaded, but he pulls the same sled at a speed of 10 miles per hour if the sled is fully loaded. If Toby takes a continuous 4-part journey, first pulling the loaded sled for 180 miles, then pulling the unloaded sled for 120 miles, then pulling the loaded sled 80 miles, and finally, pulling the unloaded sled another 140 miles, how many hours in total will Toby spend pulling the sled?"""
    
    # Define Toby's speeds in miles per hour
    unloaded_speed = 20
    loaded_speed = 10
    
    # Define the distances traveled with the loaded and unloaded sleds
    loaded_distance_1 = 180 # miles
    unloaded_distance_1 = 0
    loaded_distance_2 = 80 # miles
    unloaded_distance_2 = 0
    total_unloaded_distance = 120 + 140 # miles
    
    # Calculate the time it takes for Toby to travel each distance
    time_1 = loaded_distance_1 / loaded_speed
    time_2 = unloaded_distance_1 / unloaded_speed
    time_3 = loaded_distance_2 / loaded_speed
    time_4 = unloaded_distance_2 / unloaded_speed
    total_unloaded_time = total_unloaded_distance / unloaded_speed
    
    # Calculate the total time Toby spends pulling the sled
    total_time = time_1 + time_2 + time_3 + time_4 + total_unloaded_time
    
    # Return the result
    result = round(total_time, 1)
    return result

print(solution())