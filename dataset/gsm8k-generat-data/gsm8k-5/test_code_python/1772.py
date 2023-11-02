def solution():
    distance_north = 55  # Tod drives 55 miles to the north
    distance_west = 95  # Tod drives 95 miles to the west
    speed = 25  # Tod constantly drives 25 miles per hour

    # Calculate the total time Tod spent driving
    time_drive = (distance_north + distance_west) / speed
    result = time_drive
    return result

print(solution())