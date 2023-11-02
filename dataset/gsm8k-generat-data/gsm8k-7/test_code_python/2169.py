def solution():
    distance = 5  # in miles
    john_speed = 15  # in mph
    john_time = distance / john_speed * 60  # in minutes

    second_place_time = 23  # in minutes
    john_win_time = john_time - second_place_time

    result = john_win_time
    return result

print(solution())