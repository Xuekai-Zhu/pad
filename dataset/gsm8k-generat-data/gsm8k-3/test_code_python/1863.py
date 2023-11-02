def solution():
    """Edmonton is 220 kilometers north of Red Deer. Calgary is 110 kilometers south of Red Deer. If you travel at 110 kilometers per hour, how long will it take to get from Edmonton to Calgary?"""
    # Define the distances between the cities
    EDMONTON_TO_RED_DEER = 220
    RED_DEER_TO_CALGARY = 110

    # Define the speed of travel
    SPEED = 110

    # Calculate the total distance traveled
    total_distance = EDMONTON_TO_RED_DEER + RED_DEER_TO_CALGARY

    # Calculate the time it will take to travel the total distance
    time = total_distance / SPEED

    # Display the time it will take to travel from Edmonton to Calgary
    result = time
    return result

print(solution())