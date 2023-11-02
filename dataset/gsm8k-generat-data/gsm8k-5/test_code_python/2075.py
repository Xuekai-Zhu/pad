def solution():
    hallway_length = 16  # The hallway is 16m long
    father_speed = 3  # Father walks three times as fast as the son, in meters per second
    son_speed = 1  # Son walks at 1 meter per second

    # Calculate the time it takes for them to meet in the middle of the hallway
    total_speed = father_speed + son_speed
    time_to_meet = hallway_length / total_speed

    # Calculate the distance from the father's end of the hallway where they will meet
    distance_to_meet = father_speed * time_to_meet
    result = distance_to_meet
    return result

print(solution())