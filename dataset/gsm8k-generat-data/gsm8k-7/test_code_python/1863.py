def solution():
    edmonton_to_red_deer_distance = 220
    calgary_to_red_deer_distance = 110
    speed = 110

    # Calculate the total distance to be travelled
    total_distance = edmonton_to_red_deer_distance + calgary_to_red_deer_distance

    # Calculate the time it will take to travel the distance at the given speed
    time_in_hours = total_distance / speed
    result = time_in_hours
    return result

print(solution())