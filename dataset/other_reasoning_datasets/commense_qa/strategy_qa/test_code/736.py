def solution():
    pyrenees_width = 305
    runner_speed = 8.33 #(in miles per hour)
    time_to_cover_pyrenees = pyrenees_width / runner_speed #(in hours)
    if time_to_cover_pyrenees <= 24:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())