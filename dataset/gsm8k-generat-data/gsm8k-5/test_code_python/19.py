def solution():
    # Calculate the total distance Tim bikes to work in a week
    work_distance = 20 * 2 * 5  # Tim bikes back and forth to work for 5 days, 20 miles each way

    # Calculate the total distance Tim bikes on his weekend ride
    weekend_distance = 200

    # Calculate the total time Tim spends biking in a week
    total_distance = work_distance + weekend_distance
    total_time = total_distance / 25  # Tim bikes at 25 mph
    result = total_time
    return result

print(solution())