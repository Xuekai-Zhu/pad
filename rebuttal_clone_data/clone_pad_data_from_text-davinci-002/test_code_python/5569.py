def solution():
    hours = 2790 / 62
    rest_stops = hours / 5
    rest_time = rest_stops * 30
    search_time = 30
    total_time = hours + rest_time + search_time
    result = total_time
    return result

print(solution())