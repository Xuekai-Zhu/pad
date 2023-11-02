def solution():
    """Jake's dad can drive the distance from their house to the water park in 30 minutes. He spends half that journey driving 28 miles per hour and the other half driving 60 miles per hour on the highway. If Jake can bike 11 miles per hour, how many hours will it take him to bike to the water park?"""
    # Define the distance to the water park
    distance = None

    # Define the time taken by Jake's dad to drive to the water park
    driving_time = 0.5  # 30 minutes = 0.5 hours

    # Calculate the distance covered by Jake's dad driving at 28 miles per hour
    distance_covered_1 = driving_time * 28

    # Calculate the distance covered by Jake's dad driving at 60 miles per hour
    distance_covered_2 = driving_time * 60

    # Calculate the total distance covered by Jake's dad
    total_distance_covered = distance_covered_1 + distance_covered_2

    # Calculate the remaining distance that Jake needs to bike
    distance = distance - total_distance_covered

    # Calculate the time taken by Jake to bike the remaining distance
    biking_time = distance / 11
    
    # return the result
    result = biking_time
    return result

print(solution())