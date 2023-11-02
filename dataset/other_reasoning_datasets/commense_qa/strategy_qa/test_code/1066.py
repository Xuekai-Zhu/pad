def solution():
    conan_air_time = 11
    children_bedtime = 10
    if conan_air_time > children_bedtime:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())