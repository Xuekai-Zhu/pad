def solution():
    # Calculate the total driving time and distance
    driving_time = 2 * 5  # the bus driver drives an average of 2 hours each day, 5 days a week
    distance_mon_to_wed = 12 * driving_time * 3  # from Monday to Wednesday he drove at an average speed of 12 kilometers per hour
    distance_thu_to_fri = 9 * driving_time * 2  # from Thursday to Friday at an average speed of 9 kilometers per hour
    total_distance = distance_mon_to_wed + distance_thu_to_fri

    result = total_distance
    return result

print(solution())