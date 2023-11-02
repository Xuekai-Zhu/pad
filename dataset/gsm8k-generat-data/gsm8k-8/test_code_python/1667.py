def solution():
    # Calculate officer A's average speed
    officerA_speed = 36 / 4

    # Calculate officer B's average speed
    officerB_speed = 55 / 5

    # Calculate the total number of streets both officers will patrol in one hour
    total_streets_per_hour = officerA_speed + officerB_speed

    result = total_streets_per_hour
    return result

print(solution())