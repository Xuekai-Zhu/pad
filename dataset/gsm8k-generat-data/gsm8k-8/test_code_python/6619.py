def solution():
    # Calculate the number of trips needed to transport all the cattle
    num_trips = 400 // 20

    # Calculate the total driving distance
    total_distance = num_trips * 60

    # Calculate the total driving time
    driving_time = total_distance / 60

    result = driving_time
    return result

print(solution())