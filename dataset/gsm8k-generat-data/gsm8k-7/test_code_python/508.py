def solution():
    time_first_leg = 0.5  # half an hour
    speed_first_leg = 30

    time_second_leg = time_first_leg * 2  # twice as long
    speed_second_leg = speed_first_leg * 2  # twice the speed

    # Calculate the distance covered in the first leg of the trip
    distance_first_leg = time_first_leg * speed_first_leg

    # Calculate the distance covered in the second leg of the trip
    distance_second_leg = time_second_leg * speed_second_leg

    # Calculate the total distance covered
    total_distance = distance_first_leg + distance_second_leg
    result = total_distance
    return result

print(solution())