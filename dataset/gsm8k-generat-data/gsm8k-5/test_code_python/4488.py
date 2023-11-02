def solution():
    speed_janet = 30  # Janet is driving a speedboat at 30 miles per hour
    speed_sister = 12  # Janet's sister is sailing at 12 miles per hour
    distance = 60  # The lake is 60 miles wide

    # Calculate the time it takes Janet to cross the lake
    time_janet = distance / speed_janet

    # Calculate the distance the sister covers in the same time
    distance_sister = speed_sister * time_janet

    # Calculate the time Janet has to wait
    time_wait = time_janet * (distance_sister / distance - 1)
    result = time_wait
    return result

print(solution())