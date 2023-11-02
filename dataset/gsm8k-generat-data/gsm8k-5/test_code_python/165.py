def solution():
    total_distance = 55 + 10  # Manex will drive a total of 65 miles
    driving_time = total_distance * 2  # Manex can drive 1 mile in 2 minutes
    time_at_destination = 2  # Manex will stay for 2 hours at the destination
    total_time = (driving_time + (time_at_destination * 60)) / 60  # Convert total time from minutes to hours

    result = total_time
    return result

print(solution())