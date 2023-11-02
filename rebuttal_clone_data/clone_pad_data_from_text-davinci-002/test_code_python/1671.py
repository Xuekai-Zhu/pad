def solution():
    end_point = 80
    initial_point = 50
    change_in_width = 2
    meters_per_second = 5
    total_distance = (end_point - initial_point)/change_in_width
    total_time = total_distance/meters_per_second
    result = total_time
    return result

print(solution())