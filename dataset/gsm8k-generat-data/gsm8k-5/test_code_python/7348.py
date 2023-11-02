def solution():
    distance_yesterday = 12  # Amy biked 12 miles yesterday
    distance_today = 2 * distance_yesterday - 3  # Amy biked 3 miles less than twice yesterday's distance

    # Calculate the total distance Amy biked in two days
    total_distance = distance_yesterday + distance_today
    result = total_distance
    return result

print(solution())