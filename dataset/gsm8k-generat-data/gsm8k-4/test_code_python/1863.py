def solution():
    """Edmonton is 220 kilometers north of Red Deer. Calgary is 110 kilometers south of Red Deer. If you travel at 110 kilometers per hour, how long will it take to get from Edmonton to Calgary?"""
    # Define the distances
    edmonton_distance = 220
    calgary_distance = 110

    # Calculate the total distance to travel
    total_distance = edmonton_distance + calgary_distance

    # Calculate the time it will take to travel the distance at a speed of 110 km/hr
    time = total_distance / 110

    # return the result
    result = time
    return result

print(solution())