def solution():
    distance = 60
    time = 1
    # Using formula distance = speed * time, we can find the speed
    # Speed is equal to the distance divided by the time taken to cover that distance
    actual_speed = distance / time
    # We know that Natasha was going 10 mph over the speed limit, so we can find the speed limit by subtracting 10 from the actual speed
    speed_limit = actual_speed - 10
    result = speed_limit
    return result

print(solution())