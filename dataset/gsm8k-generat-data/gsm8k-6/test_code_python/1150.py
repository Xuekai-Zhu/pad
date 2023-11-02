def solution():
    # Calculate the total distance travelled by the driver in a week
    distance_mon = 30 * 3 + 25 * 4  # distance travelled on Monday
    distance_tue = 30 * 3 + 25 * 4  # distance travelled on Tuesday
    distance_wed = 30 * 3 + 25 * 4  # distance travelled on Wednesday
    distance_thu = 30 * 3 + 25 * 4  # distance travelled on Thursday
    distance_fri = 30 * 3 + 25 * 4  # distance travelled on Friday
    distance_sat = 30 * 3 + 25 * 4  # distance travelled on Saturday
    total_distance = distance_mon + distance_tue + distance_wed + distance_thu + distance_fri + distance_sat
    result = total_distance
    return result

print(solution())