def solution():
    """Jake's dad can drive the distance from their house to the water park in 30 minutes. He spends half that journey driving 28 miles per hour and the other half driving 60 miles per hour on the highway. If Jake can bike 11 miles per hour, how many hours will it take him to bike to the water park?"""
    # Define the distance from home to water park in miles
    distance = 15

    # Calculate the time it takes for Jake's dad to drive half the distance at 28 mph and the other half at 60 mph
    time_driving_28mph = 0.5 * (distance / 28) 
    time_driving_60mph = 0.5 * (distance / 60) 
    total_time = time_driving_28mph + time_driving_60mph

    # Calculate the time it takes for Jake to bike the distance
    jake_time = distance / 11

    # Calculate the total time it takes for Jake to get to the water park
    total_time += jake_time

    # Display the total time
    result = total_time
    return result

print(solution())