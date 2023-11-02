def solution():
    unloaded_speed = 20
    loaded_speed = 10

    # Calculate the time it takes to pull the loaded sled for 180 miles
    loaded_time1 = 180 / loaded_speed

    # Calculate the time it takes to pull the unloaded sled for 120 miles
    unloaded_time1 = 120 / unloaded_speed

    # Calculate the time it takes to pull the loaded sled for 80 miles
    loaded_time2 = 80 / loaded_speed

    # Calculate the time it takes to pull the unloaded sled for 140 miles
    unloaded_time2 = 140 / unloaded_speed

    # Calculate the total time Toby spends pulling the sled for the entire journey
    total_time = loaded_time1 + unloaded_time1 + loaded_time2 + unloaded_time2
    result = total_time
    return result

print(solution())