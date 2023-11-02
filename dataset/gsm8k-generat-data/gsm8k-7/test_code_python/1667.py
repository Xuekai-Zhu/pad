def solution():
    officerA_streets_per_hour = 36 / 4
    officerB_streets_per_hour = 55 / 5

    # Calculate the total number of streets both officers will patrol in one hour
    total_streets_per_hour = officerA_streets_per_hour + officerB_streets_per_hour
    result = total_streets_per_hour
    return result

print(solution())