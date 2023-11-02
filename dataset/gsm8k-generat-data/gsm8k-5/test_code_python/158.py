def solution():
    total_distance = 150  # Jerome is taking a 150-mile bicycle trip
    planned_distance = 12 * 12  # Jerome plans to ride 12 miles for 12 days
    remaining_distance = total_distance - planned_distance  # Jerome has to ride the remaining distance

    # Calculate the distance Jerome needs to ride on the 13th day
    distance_on_13th_day = remaining_distance % 12

    result = distance_on_13th_day
    return result

print(solution())