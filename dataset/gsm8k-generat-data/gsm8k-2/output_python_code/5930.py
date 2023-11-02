def solution():
    """Jake's dad can drive the distance from their house to the water park in 30 minutes. He spends half that journey driving 28 miles per hour and the other half driving 60 miles per hour on the highway. If Jake can bike 11 miles per hour, how many hours will it take him to bike to the water park?"""
    total_distance = 15 #30 min = 0.5 hr, so total distance = 30 min * dad's speed = 0.5 * dad's speed
    time_at_28mph = total_distance / (2*28)
    time_at_60mph = total_distance / (2*60)
    total_time = time_at_28mph + time_at_60mph
    jake_speed = 11
    jake_time = total_distance / jake_speed
    result = jake_time
    return result

print(solution())