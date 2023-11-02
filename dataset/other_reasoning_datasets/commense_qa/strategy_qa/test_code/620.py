def solution():
    olympic_stadium_capacity = 74000
    superbowl_attendance = 62417
    if superbowl_attendance > olympic_stadium_capacity:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())