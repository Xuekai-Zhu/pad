def solution():
    hallway_length = 16
    son_speed = 1
    father_speed = 3

    total_speed = son_speed + father_speed
    time_taken = hallway_length / total_speed

    distance_from_father_end = father_speed * time_taken
    result = distance_from_father_end
    return result

print(solution())