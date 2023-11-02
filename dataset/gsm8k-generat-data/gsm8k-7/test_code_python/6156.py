def solution():
    first_leg_distance = 60 * 3  # distance covered in the first 3 hours
    total_distance = first_leg_distance + (x * 2)  # total distance covered in 5 hours with a speed of x in the next 2 hours
    total_time = 5  # total time taken to cover the distance of 5 hours
    avg_speed = 70  # average speed required for the journey

    # Calculate the required speed for the next 2 hours
    required_speed = (avg_speed * total_time - first_leg_distance) / 2
    result = required_speed
    return result

print(solution())