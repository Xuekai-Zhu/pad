def solution():
    total_distance = 35
    num_portions = 5
    portion_distance = total_distance / num_portions
    speed = 40
    time = 0.7

    # Calculate the distance that Abel has traveled
    distance_traveled = speed * time

    # Calculate the number of portions that Abel has covered
    num_portions_covered = distance_traveled / portion_distance
    result = num_portions_covered
    return result

print(solution())