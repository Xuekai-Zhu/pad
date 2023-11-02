def solution():
    """Toby, the Alaskan Malamute, can pull a sled at a speed of 20 miles per hour if the sled is unloaded, but he pulls the same sled at a speed of 10 miles per hour if the sled is fully loaded. If Toby takes a continuous 4-part journey, first pulling the loaded sled for 180 miles, then pulling the unloaded sled for 120 miles, then pulling the loaded sled 80 miles, and finally, pulling the unloaded sled another 140 miles, how many hours in total will Toby spend pulling the sled?"""
    unloaded_speed = 20
    loaded_speed = 10
    
    time_loaded_1 = 180 / loaded_speed
    time_unloaded_1 = 0
    time_loaded_2 = 80 / loaded_speed
    time_unloaded_2 = 0
    time_unloaded_3 = 120 / unloaded_speed
    time_loaded_3 = 0
    time_unloaded_4 = 140 / unloaded_speed

    total_time = time_loaded_1 + time_unloaded_1 + time_loaded_2 + time_unloaded_2 + time_unloaded_3 + time_loaded_3 + time_unloaded_4
    result = total_time
    
    return result

print(solution())