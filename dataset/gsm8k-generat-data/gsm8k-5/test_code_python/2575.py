def solution():
    total_distance = 35  # The journey is 35 miles
    portion_distance = total_distance / 5  # The journey is divided into 5 equal portions
    speed = 40  # Abel's driving speed is 40 miles per hour
    time_elapsed = 0.7  # Abel has traveled for 0.7 hours

    # Calculate the distance Abel has covered
    distance_covered = speed * time_elapsed

    # Calculate the number of portions Abel has covered
    portions_covered = distance_covered / portion_distance
    result = portions_covered
    return result

print(solution())