def solution():
    # Calculate the distance ran and walked by Ms. Warren
    distance_ran = (6 / 60) * 20  # Convert 20 minutes to hours and calculate distance ran
    distance_walked = (2 / 60) * 30  # Convert 30 minutes to hours and calculate distance walked
    total_distance = distance_ran + distance_walked  # Calculate total distance
    result = total_distance
    return result

print(solution())