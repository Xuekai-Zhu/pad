def solution():
    """Jake's dad can drive the distance from their house to the water park in 30 minutes. He spends half that journey driving 28 miles per hour and the other half driving 60 miles per hour on the highway. If Jake can bike 11 miles per hour, how many hours will it take him to bike to the water park?"""
    total_distance = 0.5 * 28 / 2 + 0.5 * 60 / 2
    jake_speed = 11
    time_taken = total_distance / jake_speed
    result = time_taken
    return result

print(solution())