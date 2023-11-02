def solution():
    # Calculate the time it takes to pull the loaded sled
    loaded_time = 180 / 10 + 80 / 10

    # Calculate the time it takes to pull the unloaded sled
    unloaded_time = 120 / 20 + 140 / 20

    # Calculate the total time Toby spends pulling the sled
    total_time = loaded_time + unloaded_time
    result = total_time
    return result

print(solution())