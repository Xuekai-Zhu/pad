def solution():
    min_driving_age = 16
    min_working_age = 14
    if min_driving_age <= min_working_age:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())