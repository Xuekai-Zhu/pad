def solution():
    total_distance = 150
    daily_distance = 12

    # Calculate the distance already covered in 12 days
    covered_distance = daily_distance * 12

    # Calculate the remaining distance
    remaining_distance = total_distance - covered_distance

    # Calculate the distance to ride on the 13th day
    distance_on_13th_day = remaining_distance

    result = distance_on_13th_day
    return result

print(solution())