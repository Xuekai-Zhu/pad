def solution():
    """Toby, the Alaskan Malamute, can pull a sled at a speed of 20 miles per hour if the sled is unloaded, but he pulls the same sled at a speed of 10 miles per hour if the sled is fully loaded. If Toby takes a continuous 4-part journey, first pulling the loaded sled for 180 miles, then pulling the unloaded sled for 120 miles, then pulling the loaded sled 80 miles, and finally, pulling the unloaded sled another 140 miles, how many hours in total will Toby spend pulling the sled?"""
    loaded_speed = 10
    unloaded_speed = 20
    loaded_distance = 260
    unloaded_distance = 260
    loaded_time = loaded_distance / loaded_speed
    unloaded_time = unloaded_distance / unloaded_speed
    total_time = loaded_time * 2 + unloaded_time * 2
    result = total_time
    return result

print(solution())