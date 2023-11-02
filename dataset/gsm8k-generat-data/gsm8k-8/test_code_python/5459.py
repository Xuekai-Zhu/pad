def solution():
    # Calculate the total hours the bus driver drove in a week
    total_hours = 2 * 5

    # Calculate the total distance traveled from Monday to Wednesday
    distance_mon_to_wed = 12 * 6

    # Calculate the total distance traveled from Thursday to Friday
    distance_thurs_to_fri = 9 * 4

    # Calculate the total distance traveled in the week
    total_distance = distance_mon_to_wed + distance_thurs_to_fri

    # Calculate the average distance traveled per day
    avg_distance = total_distance / 5

    result = avg_distance
    return result

print(solution())