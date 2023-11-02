def solution():
    yesterday_distance = 12
    today_distance = (2*yesterday_distance) - 3 # biking 3 miles less than twice as far as yesterday
    total_distance = yesterday_distance + today_distance
    result = total_distance
    return result

print(solution())