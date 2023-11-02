def solution():
    num_pictures = 960
    time_per_picture = 2  # minutes
    minutes_total = num_pictures * time_per_picture
    hours_total = minutes_total / 60
    result = hours_total
    return result

print(solution())