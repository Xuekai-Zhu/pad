def solution():
    # Calculate the total distance driven by the bus
    total_distance = 55 + 10  # 55 miles to the destination and 10 miles back

    # Calculate the total driving time
    driving_time = total_distance * 2  # 1 mile for 2 minutes

    # Calculate the total time including the 2 hours stay at the destination
    total_time = driving_time + 2*60  # stayed 2 hours at the destination

    # Convert the total time in minutes to hours
    total_time_hours = total_time / 60

    result = total_time_hours
    return result

print(solution())